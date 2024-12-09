'''
Exemple : 
t=[1,2,3,4]
k=generate_perfect_tree(t) :
             1
          /      \
        2          2
      /   \       /  \
    3      3     3    3
  /  \   /  \  /  \  /  \
 4   4  4   4 4   4  4   4 
 
 operation(k) :
              1
          /      \
        3          2
      /   \       /  \
    6      9     5    6
  /  \   /  \  /  \  /  \
 10  24 13  36 9  20 10 24
 
10 = 1+2+3+4 
24 = (1+2+3)*4 
13 = (1+2)*(3)+4 
etc...

feuilles(operation(k)) = [10,24,13,36,9,20,10,24]
'''

class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def Print(self):
        def dfs(node, level=0):
            if node is None:
                return
            dfs(node.right, level + 1)
            print(" \t " * level + str(node.val))
            dfs(node.left, level + 1)

        dfs(self)


def generate_perfect_tree(arr, level=0, max_level=None):
    if max_level is not None and level >= max_level:
        return None
    if not arr:
        return None

    val = arr[level % len(arr)]
    root = Tree(val)
    root.left = generate_perfect_tree(arr, level + 1, max_level)
    root.right = generate_perfect_tree(arr, level + 1, max_level)
    return root


def operation(t):
    if t is None or (t.left is None and t.right is None):
        return t

    if t.left is not None:
        #print(f"Modification gauche : {t.left.val} += {t.val}")
        t.left.val += t.val
        operation(t.left)

    if t.right is not None:
       # print(f"Modification droite : {t.right.val} *= {t.val}")
        t.right.val *= t.val
        operation(t.right)

    return t

def feuilles(tree) :
    if tree == None :
        return []
    if tree.left==None and tree.right==None :
        return [tree.val]
    return feuilles(tree.left)+feuilles(tree.right)
def sol(t) :
    t = t.split(': ')
    s = int(t[0])
    t.pop(0)
    t=''.join(t).split(' ')
    for i in range(len(t)) :
        t[i]=int(t[i])
    k=feuilles(operation(generate_perfect_tree(t,max_level=len(t))))
    ar = operation(generate_perfect_tree(t, max_level=len(t)))
    if s in k :
        return s
    return 0
    
    
f = open('day7.txt','r').readlines()
somme = 0
for i in range(len(f )):
    elem=f[i]
    print(len(f)-i)
    somme+=sol(elem)
    
print(somme)