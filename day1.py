def sol1(t, k):
    t.sort()
    k.sort()
    s = 0
    for i in range(len(t)):
        s += abs(t[i] - k[i])
    return s


def sol2(t, k):
    s = 0
    for elem in t:
        s += elem * k.count(elem)
    return s

if __name__ == '__main__':
    t = []
    k = [] 

    with open("day1.txt", 'r') as n:
        for elem in n:
            l = elem.split("  ")
            t.append(int(l[0]))
            k.append(int(l[1]))
    print(sol1(t,k),sol2(t, k))
