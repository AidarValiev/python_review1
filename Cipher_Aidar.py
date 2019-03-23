def next_sym(inch, a=1, num=0):
    if inch.isalpha():
        if num:
            return ord(inch.lower()) - ord('a')
        if inch.upper() == inch:
            return chr((ord(inch) - ord('A') + a) % 26 + ord('A'))
        return chr((ord(inch) - ord('a') + a) % 26 + ord('a'))
    return inch


def caesar(instr, a, rev=0):
    b = str(a)
    if b.isdigit():
        b = int(b)
    else:
        raise ValueError("Key should be digit")
    key = (1 - 2 * rev) * b
    return ''.join([next_sym(x, key) for x in instr])


def vigenere(instr, keystr='', rev=0):
    klist = [next_sym(x, num=1) for x in keystr]
    n = len(keystr)
    ans = str()
    for i, x in enumerate(instr):
        ans += next_sym(x, (1 - 2 * rev) * klist[i % n])
    return ans
