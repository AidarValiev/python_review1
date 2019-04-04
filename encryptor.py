import frequency
import argparse
from my_ciphers import ciphers


def read_file(path):
    ans = ''
    if path:
        with open(path, 'r') as file:
            for line in file:
                ans += line
    else:
        ans = input()
    return ans


def write_file(path, message):
    if path:
        with open(path, 'w') as file:
            file.write(message)
    else:
        print(message)


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
    namespace = parser.parse_args(input().split(' '))

    if namespace.command in ['encode', 'decode']:
        if namespace.cipher not in ciphers():
            raise ValueError("Cipher is not supported")
        rev = 0
        if namespace.command == 'decode':
            rev = 1
        instr = read_file(namespace.input_file)
        ans = ciphers()[namespace.cipher](instr, namespace.key, rev)
        write_file(namespace.output_file, ans)

    elif namespace.command == 'train':
        instr = ''
        if namespace.text_file:
            instr = read_file(namespace.text_file)
        else:
            instr = input()
        a = frequency.find_frequencies(instr)
        with open(namespace.model_file, 'w') as file:
            for char in a:
                file.write(char + ' ' + str(a.get(char, 0)) + '\n')

    elif namespace.command == 'hack':
        instr = read_file(namespace.input_file)
        ans = 0
        model_table = frequency.getfr(namespace.model_file)
        n = len(model_table)
        bestdiff = frequency.find_diff(model_table, frequency.find_frequencies(ciphers()['caesar'](instr, 0)))
        for i in range(1, n):
            newdiff = frequency.find_diff(model_table, frequency.find_frequencies(ciphers()['caesar'](instr, i)))
            if newdiff < bestdiff:
                bestdiff = newdiff
                ans = i
        write_file(namespace.output_file, ciphers()['caesar'](instr, ans))

    else:
        raise ValueError("incorrect command")
