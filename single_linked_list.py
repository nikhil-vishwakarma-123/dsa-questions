class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class List:
    def __init__(self,node = None):
        self.head = node

    def insert_node(self,data_value):
        if (self.head == None):
            self.head = Node(data_value)
        else:
            current_node = self.head
            while (current_node.next!=None):
                current_node = current_node.next
            else:
                current_node.next = Node(data_value)

    def display(self):
        current_node = self.head
        while (current_node!=None):
            print (current_node.data, end = '-->')
            current_node = current_node.next
        print('')

    def pop(self):
        current_node = self.head
        if (current_node == None):
            print ('The linked list is empty')

        while (current_node != None):
            if current_node.next.next == None:
                current_node.next = None
                break
            current_node = current_node.next

    def remove(self,value):
        current_node = self.head
        if (current_node == None):
            print ('The linked list is empty')

        while (current_node!=None):
            if (current_node.data == value):
                if (current_node.next==None):
                    self.head = None
                else:
                    current_node.data = current_node.next.data
                    current_node.next = current_node.next.next
            else:
                current_node = current_node.next

    def insert_at_node(self,node_no, data):
        current_node = self.head
        count = 0
        if ((current_node == None) and (node_no==1)):
            self.head = Node(data)
        elif ((current_node == None) and (node_no>1)):
            print ('Current Linked list is shorter than you thought!')
        else:
            while (current_node!=None):
                count += 1
                if (count==node_no):
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return 0
                current_node = current_node.next




l1 = List(Node(1))

l1.insert_node(2)
l1.insert_node(3)
l1.insert_node(4)
l1.display()
l1.pop()
l1.display()
l1.pop()
l1.display()
l1.insert_node(5)
l1.insert_node(6)
l1.insert_node(7)
l1.display()
l1.remove(6)
l1.display()
l1.insert_at_node(3,100)
l1.display()
l1.insert_at_node(4,1131200)
l1.display()
l1.insert_at_node(1,98765)
l1.display()
l1.head = None
l1.pop()

