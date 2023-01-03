class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + int(tree.cargo)


"""Префиксная запись"""


def prefix_tree(tree):
    if tree is None: return 0
    print(tree.cargo)
    prefix_tree(tree.left)
    prefix_tree(tree.right)


"""Постфиксная запись"""


def postfix_tree(tree):
    if tree is None: return 0
    postfix_tree(tree.left)
    postfix_tree(tree.right)
    print(tree.cargo)


"""Постфиксная запись"""


def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.cargo)
    print_tree_inorder(tree.right)


def infix_tree(tree, level=0):
    if tree is None: return 0
    infix_tree(tree.right, level+1)
    #print(tree.cargo, level+1)
    print('  ' * level + str(tree.cargo))
    infix_tree(tree.left, level+1)


# tree = Tree(1, Tree(2), Tree(3))
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
print_tree_inorder(tree)
infix_tree(tree)
