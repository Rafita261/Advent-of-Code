def printf(t) :
    for elem in t :
        print("".join(elem))
    print("\n")
gv=0
def move(gird,y,x) :
    global gv
    mv = gird[y][x]
    if mv == 'v' :
        if y==len(gird[0])-1 :
            gv+=1
            return False
        if gird[y+1][x]=='X' :
            gv+=1
            printf(gird)
        if gird[y+1][x] == '#' :
            gird[y][x] = '<'
            gv+=1
            return True
        gird[y+1][x]='v'
        gird[y][x]='X'
        return True
    if mv == '^' :
        if y==0 :
            gv+=1
            return False
        if gird[y-1][x]=='X' :
            gv+=1
            printf(gird)
        if gird[y-1][x]=='#' :
            gird[y][x]='>'
            gv+=1
            return True
        gird[y-1][x]='^'
        gird[y][x]='X'
        return True
    if mv == '<' :
        if x==0 :
            gv+=1
            return False
        if gird[y][x-1]=='X' :
            gv+=1
            printf(gird)
        if gird[y][x-1] == '#' :
            gird[y][x]='^'
            gv+=1
            return True
        gird[y][x-1]='<'
        gird[y][x]='X'
        return True
    if mv == '>' :
        if x==len(gird)-1:
            gv+=1
            return False
        if gird[y][x+1]=='X' :
            gv+=1
            printf(gird)
        if gird[y][x+1]=='#' :
            gird[y][x]='v'
            gv+=1
            return True
        gird[y][x+1]='>'
        gird[y][x]='X'
        return True

def get_pos(gird) :
    for i in range(len(gird)) :
        for j in range(len(gird[0])) :
            ch = gird[i][j]
            if ch !='.' and ch !='#' and ch != 'X' :
                return (i,j)

def remove(gird) :
    x,y = get_pos(gird)
    while move(gird, x,y) :
        x,y = get_pos(gird)
    return gird

f = open('day6.txt','r')
sinp = ''.join(f.readlines()).splitlines()
sinp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
.........
......#...
""".split('\n')
for i in range(len(sinp)) :
    sinp[i]=list(sinp[i])

s=0
for elem in remove(sinp) :
    s+=elem.count('O')
    
print((gv//2)+1)