from collections import Counter
import string


# string of symbols that are supported by encryption
encrypted_symbols = string.ascii_lowercase


# searches next symbol in cycled alphabet of encrypted symbols
def next_symbol(symbol, step=1):
    low = symbol.lower()
    pos = encrypted_symbols.find(low)
    if pos != -1:
        next_s = encrypted_symbols[(pos + step) % len(encrypted_symbols)]
        return next_s.lower() if low == symbol else next_s.upper()
    return symbol


# returns counter with frequencies of encrypted symbols
def find_frequencies(message):
    counts = Counter((x for x in message if x in encrypted_symbols))
    total_count = sum(counts.values())
    for sym in counts:
        counts[sym] /= total_count
    return counts


# gets counter with frequencies from file
def get_frequencies(path):
    counts = Counter()
    with open(path, 'r') as file:
        for line in file:
            char, count = line.split(' ')
            counts[char] = float(count)
    return counts


# finds shift with best(least) difference between two tables of frequencies
def best_diff(first_table, second_table):
    best_sum = -1
    best_shift = 0
    for shift in range(len(encrypted_symbols)):
        sum = 0
        for symbol in encrypted_symbols:
            sum += (first_table.get(next_symbol(symbol, shift), 0) - second_table.get(symbol, 0)) ** 4
        if best_sum == -1 or best_sum > sum:
            best_sum = sum
            best_shift = shift
    return best_shift
