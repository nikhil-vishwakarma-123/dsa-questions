class Node:
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleList:
    def __init__(self, head = None):
        self.head = head

    def display(self):
        current_node = self.head
        while (current_node.data!=None):
            print (current_node.data)
            current_node = current_node.next

    def previous(self):
        current_node = self.head.previous


dl1 = DoubleList(Node(1))
dl1.display()
