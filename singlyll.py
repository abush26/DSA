class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
       
class linkedlist:
    def __init__(self):
        self.head = None
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(5)
        node5 = Node(6)
        self.head = node1
        node1.next = node2
       
        node2.next = node3
       
        node3.next = node4
        
        node4.next = node5
    def display(self):
        if self.head == None:
            print("Empty Linked List")        
        else:
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next

    def insert_at_begin(self):
        new_node = Node(3)
        new_node.next =self.head
        self.head = new_node
    def insert_at_end(self):
        new_node = Node(7)
        if self.head is None:
            
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def insert_at_position(self , pos , data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp= temp.next
        np.data = data
        np.next = temp.next
        temp.next = np
    def delete_at_begin(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
    def delete_at_end(self):
        if self.head is None:
            print("Empty Linked list" )
        else:
            temp = self.head.next
            temp2 = self.head
            while temp.next:
                temp = temp.next
                temp2 = temp2.next
            temp2.next = None
    def delect_at_position(self , pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
   


element = linkedlist()

element.insert_at_end()
element.delete_at_begin()
element.insert_at_position(4 , 25 )
element.insert_at_begin()

element.insert_at_end()
element.delect_at_position(3)
element.display()