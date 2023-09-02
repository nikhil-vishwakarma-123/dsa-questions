class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self,head,end):
        self.head = None
        self.end = None

    def push(self,data):
        if (self.end != None):
            new_node = Node(data)
            self.end.next = new_node
            self.end = new_node
        else:
            self.head = self.end = Node(data)

