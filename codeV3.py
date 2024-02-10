import random
import string


def generate(alph,s):

    #ex_lib = {"a": "b","b":"d"}
    lib = {}
    new_seed = random.random()
    cache = list(alph)
    for letter in alph:
        random.seed(new_seed)
        x = random.randint(0,len(cache)-1)
        lib[letter] = cache[x]
        cache.remove(cache[x])
        new_seed = random.random()
    return(lib, new_seed)

def encode(text, seed):
    alphabet = list(string.printable)
    alphabet.remove('\t')
    alphabet.remove('\n')
    alphabet.remove('\r')
    alphabet.remove('\x0b')
    alphabet.remove('\x0c')
    alphabet.remove('\\')
    cache = list(alphabet)
    
    random.seed(seed)
    new_seed = random.random() 
    message = []

    for t in text:
        lib, new_seed = generate(cache, new_seed)
        message.append(lib[t])

    final = "".join(message)
    return final

def decode(text, seed):
    alphabet = list(string.printable)
    alphabet.remove('\t')
    alphabet.remove('\n')
    alphabet.remove('\r')
    alphabet.remove('\x0b')
    alphabet.remove('\x0c')
    alphabet.remove('\\')

    cache = list(alphabet)

    random.seed(seed)
    new_seed = random.random()

    message = []

    for l in text:
        lib, new_seed = generate(cache, new_seed)
        keys = list(lib.keys())
        values = list(lib.values())
        pos = values.index(l)
        message.append(keys[pos])
    final = "".join(message)
    return final


if __name__ == "__main__":
    sed = "sus"
    coded = "y.Ck]S"
    print(encode("amogus",sed))
    print(decode(coded,sed))
