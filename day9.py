def fic(k) :
    k=str(k)
    s=""
    id = 0
    for i in range(len(k)) :
        elem = int(k[i])
        if i%2 != 0 :
            s+='.'*elem
        else :
            s+=str(id)*elem
            id+=1
    return list(s)
def permut(t,i,j) :
    c=t[i]
    t[i]=t[j]
    t[j]=c

def compact(f) :
    s=0
    for i in range(len(f)-f.count('.')-1) :
        if f[i]=='.' :
            while f[len(f)-1] == '.' :
                f.pop(-1)
            permut(f,i,len(f)-1)
            f.pop(len(f)-1)
            print(''.join(f))
    for i in range(len(f)) :
        s+=(i*int(f[i]))
    return s
k = open("day9.txt","r")
print(compact(fic(k)))