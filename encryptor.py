import argparse
from my_ciphers import ciphers, caesar
from frequency import get_frequencies, find_frequencies, best_diff, encrypted_symbols


# reads text from file or, if path is None, from input()
def read_file(path):
    if path:
        with open(path, 'r') as file:
            ans = file.read()
    else:
        ans = input()
    return ans


# write text to file or, if path is None, to output()
def write_file(path, message):
    if path:
        with open(path, 'w') as file:
            file.write(message)
    else:
        print(message)


# parses arguments
def argument_parse():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='command')
    encode_parser = subs.add_parser('encode')
    decode_parser = subs.add_parser('decode')
    hack_parser = subs.add_parser('hack')
    train_parser = subs.add_parser('train')
    encode_parser.add_argument('-c', '--cipher', required=True)
    encode_parser.add_argument('-k', '--key', required=True)
    encode_parser.add_argument('-i', '--input-file')
    encode_parser.add_argument('-o', '--output-file')
    decode_parser.add_argument('-c', '--cipher', type=str, required=True)
    decode_parser.add_argument('-k', '--key', required=True)
    decode_parser.add_argument('-i', '--input-file')
    decode_parser.add_argument('-o', '--output-file')
    hack_parser.add_argument('-i', '--input-file')
    hack_parser.add_argument('-o', '--output-file')
    hack_parser.add_argument('-m', '--model-file', required=True)
    train_parser.add_argument('-t', '--text-file')
    train_parser.add_argument('-m', '--model-file', required=True)
    namespace = parser.parse_args()
    return namespace


# encodes the message with the selected cipher
def encode(namespc):
    instr = read_file(namespc.input_file)
    write_file(namespc.output_file, ciphers[namespc.cipher](instr, namespc.key))


# decodes the message with the selected cipher
def decode(namespc):
    instr = read_file(namespc.input_file)
    write_file(namespc.output_file, ciphers[namespc.cipher](instr, namespc.key, reversed=True))


# makes model of frequencies based on entered message
def train(namespc):
    model_table = find_frequencies(read_file(namespc.text_file))
    message = ''
    for char in model_table:
        message += (char + ' ' + str(model_table.get(char, 0)) + '\n')
    write_file(namespc.model_file, message)


# decodes message, which was encrypted with caesar, with unknown key
def hack(namespc):
    instr = read_file(namespc.input_file)
    model_table = get_frequencies(namespc.model_file)
    write_file(namespc.output_file, caesar(instr, best_diff(model_table, find_frequencies(instr))))


# dict of enabled commands
commands = {'encode': encode, 'decode': decode, 'train': train, 'hack': hack}


if __name__ == '__main__':
    namespace = argument_parse()
    commands[namespace.command](namespace)
