def fic(k):
    k = str(k)
    s = []
    id = 0
    for i in range(len(k)):
        elem = int(k[i])
        if i % 2 != 0:  # Espace libre
            for _ in range(elem):
                s.append('.')
        else:  # Fichier avec ID
            for _ in range(elem):
                s.append(str(id))
            id += 1
    return s

def find_free_space(f, size):
    free_start = -1
    free_count = 0
    for i, block in enumerate(f):
        if block == '.':
            if free_start == -1:
                free_start = i
            free_count += 1
            if free_count == size:
                return free_start
        else:
            free_start = -1
            free_count = 0
    return -1

def compact_v2(f):
    files = []
    i = 0
    while i < len(f):
        if f[i] != '.':
            file_id = f[i]
            start = i
            while i < len(f) and f[i] == file_id:
                i += 1
            size = i - start
            files.append((file_id, start, size))
        else:
            i += 1
    files.sort(key=lambda x: int(x[0]), reverse=True)
    for file_id, start, size in files:
        free_start = find_free_space(f, size)
        if free_start != -1 and free_start < start :
            for i in range(size):
                f[free_start + i] = file_id
                f[start + i] = '.'

    checksum = 0
    for pos, block in enumerate(f):
        if block != '.':
            checksum += pos * int(block)
    return checksum
    
with open("day9.txt", "r") as file:
    k = file.readline().strip()

f = fic(k)
result = compact_v2(f)
print(result)
