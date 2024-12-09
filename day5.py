def Rule(X,Y,t) :
    if X not in t or Y not in t : return True
    return t.index(X)<t.index(Y)
    
f = open('fl.txt','r')
k=f.readline().replace('\n','')
rules=[]
pages=[]
while '|' in k :
    rules.append(k.split('|'))
    k=f.readline().replace('\n','')
for i in range(len(rules)) :
    rules[i][0] = int(rules[i][0])
    rules[i][1] = int(rules[i][1])
for elem in f :
    page= elem.replace("\n",'').split(',')
    for p in range(len(page)) :
        page[p] = int(page[p])
    pages.append(page)

s=0
for page in pages :
    ok = True
    for rule in rules :
        if not Rule(rule[0],rule[1],page) :
            ok = False
    if ok :
        continue 
    for _ in range(len(rules)) :
        for rule in rules :
            if not Rule(rule[0],rule[1],page) :
                k = page[page.index(rule[0])]
                page[page.index(rule[0])]=page[page.index(rule[1])]
                page[page.index(rule[1])]=k
    print(page)
    s+=page[len(page)//2]
print(s)