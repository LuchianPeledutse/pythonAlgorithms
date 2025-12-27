import numpy as np




class BinaryNode:
    """
    BinaryNode implementation. Each node has key, data and two children as attributes
    """
    def __init__(self, key: float, data: dict,
                 left: BinaryNode | None = None, right: BinaryNode | None = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    """Implementation of BinaryTree data structure"""
    def __init__(self, root: BinaryNode | None = None):
        self.root = root
    
    def inorder_walk(self, node: BinaryNode | None = None) -> None:
        if node != None:
            self.inorder_walk(node.left)
            print(node.key)
            self.inorder_walk(node.right)


root = BinaryNode(8, {"Luchian": 21, "Evelina": 11})
left_child = BinaryNode(3.14, {"Vitalie": 49})
right_child = BinaryNode(8.15, {"Luchiya": 39})

binarytree = BinaryTree(root=root)
binarytree.root.left = left_child
binarytree.root.right = right_child
print(binarytree.root.data)
print(binarytree.root.left.data)
print(binarytree.root.right.data, end = '\n\n')
binarytree.inorder_walk(binarytree.root)


'--------------------------------------------------------------------------------'