class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        self.prev = None
class Doublyll:
    def __init__(self):
        self.head = None
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(5)
        node5 = Node(6)
        self.head = node1
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node4
        node4.prev = node3
        node4.next = node5
    def insert_at_begin(self):
        new_node = Node(3)
        new_node.next =self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_end(self):
        new_node = Node(7)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def insert_at_position(self , pos , data):
       np = Node(data)
       temp = self.head
       for i in range(1 , pos-1):
           temp = temp.next
       np.prev = temp
       np.next = temp.next
       temp.next.prev = np
       temp.next = np
    def delect_at_begin(self):
        self.head = self.head.next
        self.head.prev  = None
    def delect_at_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next=None
        temp.prev = None
    def delect_at_position(self , pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None


    def display(self):
        if self.head == None:
            print("Empty Linked List")        
        else:
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next
   
element = Doublyll()
element.insert_at_begin()
element.insert_at_end()
element.delect_at_begin()
element.delect_at_end()
element.delect_at_position(2)
element.insert_at_position(3,100)
element.display()




        