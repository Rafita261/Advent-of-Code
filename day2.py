def sol1(t) :
    k = sorted(t)
    if t != k and t[::-1] != k :
        return False
    for i in range(len(t)-1):
        a = abs(int(t[i])-int(t[i+1]))
        if a != 1 and a != 2 and a != 3 :
            return False
    return True
o=0
def sol2(t) :
    global o
    if sol1(t) :
        print(t)
        o+=1
        return True
    for i in range(len(t)-1) :
        k = t[0:i]+t[i+1:len(t)]
        if sol1(k) :
            o+=1
            return True
    if sol1(t[0:-1]) :
        #print(t[0:-1])
        o+=1
        return True
    return False
f = open('day2.txt','r')
s=0
for elem in f :
    t = elem.split(" ")
    for i in range(len(t)) :
        t[i]=int(t[i])
    if sol2(t) : s+=1
print(f"\t{s}")
print(o)