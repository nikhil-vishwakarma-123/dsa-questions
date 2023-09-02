class Node:

    def __init__(self,data = None, parent = None):
        self.data = data
        self.right = None
        self.left = None

        self.parent = parent


class BST:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert_node(data,self.root)