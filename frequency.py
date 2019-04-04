from collections import Counter
import string


def encrypted_symbols():
    return string.ascii_lowercase


def find_frequencies(message):
    counts = Counter(message.lower())
    for sym in counts:
        if sym not in encrypted_symbols():
            counts[sym] = 0
    counts += Counter()
    total_count = sum(counts.values())
    for sym in counts:
        counts[sym] /= total_count
    return counts


def getfr(path):
    counts = Counter()
    with open(path, 'r') as file:
        for line in file:
            char, count = line.split(' ')
            counts[char] = float(count)
    return counts


def find_diff(trained, counts):
    diff = 0
    for char in encrypted_symbols():
        diff += (trained.get(char, 0) - counts.get(char, 0)) ** 2
    return float(diff)
