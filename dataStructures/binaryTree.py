import numpy as np
from typing import List




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
    
    def search(self, node: BinaryNode, key: int | float):
        if node == None or node.key == key:
            return node
        else:
            return self.search(node.left, key) if key < node.key else self.search(node.right, key)
    
    def tree_depth(self, node: BinaryNode) -> int:
        """
        Returns the depth of the tree starting from node

        Args
        ----
        node: BinaryNode
            Binary node to start from
        """
        return 0 if node == None else 1 + max(self.tree_depth(node.left), self.tree_depth(node.right))
    
    def get_leafs(self, node: BinaryNode, leaf_list: List | None = None) -> List:
        assert node != None, 'Node is None'
        if leaf_list == None:
            leaf_list = []

        if node.left == None and node.right == None:
            leaf_list.append(node)
        else:
            for not_none_node in filter(None, (node.left, node.right)):
                self.get_leafs(not_none_node, leaf_list=leaf_list)
            return leaf_list




if __name__ == "__main__":
    root = BinaryNode(8, {"Luchian": 21, "Evelina": 11})
    l = BinaryNode(3.14, {"Vitalie": 49})
    r = BinaryNode(8.15, {"Luchiya": 39})
    rr = BinaryNode(9, {})
    ll = BinaryNode(2, {})
    llr = BinaryNode(2.5, {})

    binarytree = BinaryTree(root=root)
    binarytree.tree_insert(binarytree, l)
    binarytree.tree_insert(binarytree, r)
    binarytree.tree_insert(binarytree, rr)
    binarytree.tree_insert(binarytree, ll)
    binarytree.tree_insert(binarytree, llr)

    print(binarytree.root.data)
    print(binarytree.root.left.data)
    print(binarytree.root.right.data, end = '\n\n')
    binarytree.inorder_walk(binarytree.root)
    print(binarytree.search(binarytree.root, 8.15).key, end = '\n\n')
    print(binarytree.tree_depth(binarytree.root), end = '\n\n')
    print([item.key for item in binarytree.get_leafs(binarytree.root)])
'--------------------------------------------------------------------------------'