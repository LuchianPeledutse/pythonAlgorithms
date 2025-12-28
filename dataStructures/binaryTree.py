import numpy as np




class BinaryNode:
    """
    BinaryNode implementation. Each node has key, data and two children as attributes
    """
    def __init__(self, key: float, data: dict, parent: BinaryNode | None = None,
                 left: BinaryNode | None = None, right: BinaryNode | None = None):
        self.key = key
        self.data = data
        self.parent = parent
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

    def tree_insert(self, tree: BinaryTree, insert_node: BinaryNode) -> BinaryTree:
        """
        Given a binaryTree and a Node to insert. Inserts it in binaryTree
        binaryTree main property still remains
        """
        parent = None
        current_node = tree.root
        # Traversing the tree to find None node 
        while current_node is not None:
            parent = current_node
            # If current node is not none move to left or right child
            # Depending on key value of inserting Node
            if insert_node.key < current_node.key:
                current_node = current_node.left
            elif insert_node.key >= current_node.key:
                current_node = current_node.right

        insert_node.parent = parent
        if parent is None: # BinaryTree is empty
            tree.root = insert_node 
        else:
            # If tree is not empty insert key to left or right depending on key value
            if insert_node.key < parent.key:
                parent.left = insert_node
            elif insert_node.key >= parent.key:
                parent.right = insert_node
        




if __name__ == "__main__":
    root = BinaryNode(8, {"Luchian": 21, "Evelina": 11})
    left_child = BinaryNode(3.14, {"Vitalie": 49})
    right_child = BinaryNode(8.15, {"Luchiya": 39})

    binarytree = BinaryTree(root=root)
    binarytree.tree_insert(binarytree, left_child)
    binarytree.tree_insert(binarytree, right_child)
    print(binarytree.root.data)
    print(binarytree.root.left.data)
    print(binarytree.root.right.data, end = '\n\n')
    binarytree.inorder_walk(binarytree.root)


'--------------------------------------------------------------------------------'