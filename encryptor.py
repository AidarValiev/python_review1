import frequency
import argparse
import Cipher_Aidar


def read_file(path):
    result = ''
    with open(path, 'r') as file:
        for line in file:
            result += line
    return result


def write_file(path, message):
    with open(path, 'w') as file:
        file.write(message)


ciphers = {'caesar': Cipher_Aidar.caesar, 'vigenere': Cipher_Aidar.vigenere}

if __name__ == '__main__':
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

    if namespace.command in ['encode', 'decode']:
        if namespace.cipher not in ciphers:
            raise ValueError("Cipher is not supported")
        rev = 0
        if namespace.command == 'decode':
            rev = 1
        ans = ''
        instr = ''
        if namespace.input_file:
            instr = read_file(namespace.input_file)
        else:
            instr = input()

        ans = ciphers[namespace.cipher](instr, namespace.key, rev)

        if namespace.output_file:
            write_file(namespace.output_file, ans)
        else:
            print(ans)

    elif namespace.command == 'train':
        instr = ''
        if namespace.text_file:
            instr = read_file(namespace.text_file)
        else:
            instr = input()
        a = frequency.find_frequencies(instr)
        with open(namespace.model_file, 'w') as file:
            for char in a:
                file.write(char + ' ' + str(a[char]) + '\n')

    elif namespace.command == 'hack':
        instr = ''
        ans = 0
        if namespace.input_file:
            instr = read_file(namespace.input_file)
        else:
            instr = input()

        model_table = frequency.getfr(namespace.model_file)
        n = len(model_table)
        bestdiff = frequency.find_diff(model_table, frequency.find_frequencies(Cipher_Aidar.caesar(instr, 0)))
        for i in range(1, n):
            newdiff = frequency.find_diff(model_table, frequency.find_frequencies(Cipher_Aidar.caesar(instr, i)))
            if newdiff < bestdiff:
                bestdiff = newdiff
                ans = i

        if namespace.output_file:
            write_file(namespace.output_file, Cipher_Aidar.caesar(instr, ans))
        else:
            print(Cipher_Aidar.caesar(instr, ans))
    else:
        raise ValueError("incorrect command")
