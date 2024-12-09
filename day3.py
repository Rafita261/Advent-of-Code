import re

def sol1(s):
    pattern = r"mul\((\d+),(\d+)\)"
    m = re.findall(pattern, s)
    total = 0
    for elem in m:
        x, y = int(elem[0]), int(elem[1])
        total += x * y
    return total

def sol2(s):
    pattern = r"do\(\)|don't\(\)"
    segments = re.split(pattern, s)
    controls = re.findall(pattern, s)
    enabled = True 
    total = 0
    for i, segment in enumerate(segments):
        if enabled:
            total += sol1(segment)
        if i < len(controls):
            if controls[i] == "do()":
                enabled = True
            elif controls[i] == "don't()":
                enabled = False
    return total

if __name__ == '__main__' :
    with open('day3.txt', 'r') as f:
        p = "".join(f.readlines())
    print(f"Première Solution : {sol1(p)}")
    print(f"Deuxième Solution : {sol2(p)}")