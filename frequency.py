from collections import Counter


def find_frequencies(message):
    encrypted_symbols = 'abcdefghijklmnopqrstuvwxyz'
    counts = Counter()
    totalcount = 0
    for char in encrypted_symbols:
        counts[char] = 0
    for char in message:
        if char.lower() in encrypted_symbols:
            counts[char.lower()] += 1
            totalcount += 1
    for pair in counts:
        counts[pair] /= totalcount
    return counts


def getfr(path):
    encrypted_symbols = 'abcdefghijklmnopqrstuvwxyz'
    counts = Counter()
    for char in encrypted_symbols:
        counts[char] = 0
    with open(path, 'r') as file:
        for line in file:
            char, count = [x for x in line.split(' ')]
            counts[char] = float(count)
    return counts


def find_diff(trained, counts):
    encrypted_symbols = 'abcdefghijklmnopqrstuvwxyz'
    diff = 0
    for char in encrypted_symbols:
        diff += (trained[char] - counts[char]) ** 2
    return float(diff)
