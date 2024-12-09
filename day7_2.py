class Tree:
    def __init__(self, val=None, left=None, right=None, concat=None):
        self.val = val
        self.left = left
        self.right = right
        self.concat = concat  # Nouvelle branche pour la concaténation

    def Print(self):
        def dfs(node, level=0):
            if node is None:
                return
            dfs(node.concat, level + 1)
            dfs(node.right, level + 1)
            print(" \t" * level + str(node.val))
            dfs(node.left, level + 1)

        dfs(self)


def generate_tree(arr, level=0, max_level=None):
    if max_level is not None and level >= max_level:
        return None
    if not arr:
        return None

    val = arr[level % len(arr)]
    root = Tree(val)
    root.left = generate_tree(arr, level + 1, max_level)
    root.right = generate_tree(arr, level + 1, max_level)
    root.concat = generate_tree(arr, level + 1, max_level)
    return root


def operation(t):
    if t is None or (t.left is None and t.right is None and t.concat is None):
        return t

    if t.left is not None:
        t.left.val += t.val  # Addition
        operation(t.left)

    if t.right is not None:
        t.right.val *= t.val  # Multiplication
        operation(t.right)

    if t.concat is not None:
        t.concat.val = int(str(t.val) + str(t.concat.val))  # Concaténation
        operation(t.concat)

    return t


def feuilles(tree):
    if tree is None:
        return []
    if tree.left is None and tree.right is None and tree.concat is None:
        return [tree.val]
    return feuilles(tree.left) + feuilles(tree.right) + feuilles(tree.concat)


def sol(t):
    t = t.split(': ')
    s = int(t[0])
    t.pop(0)
    t = ''.join(t).split(' ')
    for i in range(len(t)):
        t[i] = int(t[i])
    k = feuilles(operation(generate_tree(t, max_level=len(t))))
    if s in k:
        return s
    return 0


# Lecture du fichier d'entrée
with open('day7.txt', 'r') as fic:
    f=fic.readlines()
somme = 0
for i in range(len(f)):
    elem = f[i]
    print(len(f)-i)
    somme += sol(elem)
print(somme)
