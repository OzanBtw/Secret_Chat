import random
import string


def generate(s):
    random.seed(s)
    alphabet = list(string.printable)
    alphabet.remove('\t')
    alphabet.remove('\n')
    alphabet.remove('\r')
    alphabet.remove('\x0b')
    alphabet.remove('\x0c')
    alphabet.remove('\\')
    #ex_lib = {"a": "b","b":"d"}
    lib = {}
    cache = list(alphabet)
    for letter in alphabet:
        x = random.randint(0,len(cache)-1)
        lib[letter] = cache[x]
        cache.remove(cache[x])
    return(lib)

def encode(text,lib):
    message = []
    for l in text:
        message.append(lib[l])
    final = "".join(message)
    return final


def decode(text, lib):
    message = []
    keys = list(lib.keys())
    values = list(lib.values())
    for l in text:
        pos = values.index(l)
        message.append(keys[pos])
    final = "".join(message)
    return final


if __name__ == "__main__":
   print(generate("test"))