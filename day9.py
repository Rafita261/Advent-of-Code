def fic(k):
    k = str(k)
    s = []
    id = 0
    for i in range(len(k)):
        elem = int(k[i])
        if i % 2 != 0:
            for _ in range(elem):
                s.append('.')
        else: 
            for _ in range(elem):
                s.append(str(id))
            id += 1
    return s

def compact(f):
    i = 0
    while i < len(f):
        if f[i] == '.': 
            j = len(f) - 1
            while j > i and f[j] == '.':
                j -= 1
            if j > i:
                f[i], f[j] = f[j], '.'
        i += 1

    checksum = 0
    for pos, block in enumerate(f):
        if block != '.':
            checksum += pos * int(block)
    return checksum

if __name__=='__main__' :
    with open("day9.txt", "r") as file:
        k = file.readline().strip()
    f = fic(k)
    result = compact(f)
    print(result)
