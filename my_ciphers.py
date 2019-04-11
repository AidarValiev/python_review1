from frequency import next_symbol


# encodes/decodes entrance text with caesar cipher
# rev=True means that text will be decrypted
def caesar(instr, key, rev=False):
    b = str(key)
    if b.isdigit():
        b = int(b)
    else:
        raise ValueError("Key should be digit")
    key = (1 - 2 * rev) * b
    return ''.join([next_symbol(x, key) for x in instr])


# encodes/decodes entrance text with vigenere cipher
# rev=True means that text will be decrypted
def vigenere(instr, keystr='', rev=False):
    klist = [next_symbol(x) for x in keystr]
    n = len(keystr)
    ans = str()
    for i, x in enumerate(instr):
        ans += next_symbol(x, (1 - 2 * rev) * klist[i % n])
    return ans


# contains supported ciphers
# throws exception if cipher is not supported
class Ciphers:
    supported_ciphers = {'caesar': caesar, 'vigenere': vigenere}

    def __init__(self):
        pass

    def __getitem__(self, item):
        if item in self.supported_ciphers:
            return self.supported_ciphers[item]
        raise ValueError('unsupported cipher')
