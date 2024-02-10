import random
import string


def generate(alph,s):

    #ex_lib = {"a": "b","b":"d"}
    lib = {}
    new_seed = s
    cache = list(alph)
    all_n = []
    entropyFinal = []

    for letter in alph:
        entropy1 = list(cache)
        entropy2 = list(cache)
        entropy3 = []
        random.seed(new_seed)

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
        new_seed = random.random()
        
        entropyFinal.append(entropy3)
    for letter in cache:
        x = random.randint(0,len(entropyFinal)-1)
        lib[letter] = entropyFinal[x]
        entropyFinal.remove(entropyFinal[x])
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
        x = random.choice(lib[t])
        message.append(x)

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

    len_ = int(len(text)/2)

    for l in range(len_):
        symbol = text[l+l:l+l+2]
        
        lib, new_seed = generate(cache, new_seed)
        keys = list(lib.keys())
        values = list(lib.values())
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




if __name__ == "__main__":
    sed = "sus"
    coded1 = encode("Anan",sed)
    print(decode(coded1,sed))
