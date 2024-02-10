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
    lib = {}
    cache = []
    all_n = []
    for i in alphabet:
        entropy1 = list(alphabet)
        entropy2 = list(alphabet)
        entropy3 = []
        for t in range(5):
            while True:
                x = random.randint(0,len(entropy1)-1)
                y = random.randint(0,len(entropy2)-1)
                symbol = str(entropy1[x]) + str(entropy2[y])
                if symbol in all_n:
                    continue
                else:
                    all_n.append(symbol)
                    entropy1.remove(entropy1[x])
                    entropy2.remove(entropy2[y])
                    entropy3.append(symbol)
                    break
        cache.append(entropy3)

    for letter in alphabet:
        x = random.randint(0,len(cache)-1)
        lib[letter] = cache[x]
        cache.remove(cache[x])
    return lib

def encode(text,lib):
    message = []
    for l in text:
        x = random.choice(lib[l])
        message.append(x)
    final = "".join(message)
    return final

def decode(text, lib):
    message = []
    keys = list(lib.keys())
    values = list(lib.values())
    len_ = int(len(text)/2)
    for l in range(len_):
        symbol = text[l+l:l+l+2]
        for v in values:
            if symbol in v:
                pos = values.index(v)
                break
        try:
            message.append(keys[pos])
        except:
            message.append("")
    final = "".join(message)
    return final

#/FK!ukOD;'Z}
if __name__ == "__main__":
    text = "Amogus"
    text2 = "4,-e8<O~N!v*"
    lib = generate("a")
    print(lib)
    print(encode(text,lib))
    print(len(text2))
    print(decode(text2,lib))
    print(len(lib))

