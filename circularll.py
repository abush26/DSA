class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
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
        node5.next = self.head 
    # def insert_at_begin(self, data):
    #     new_node = Node(data)
    #     if not self.head: 
    #         self.head = new_node
    #         self.head.next = self.head  
    #         self.tail = self.head 
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #         self.tail.next = self.head
    
    # def insert_at_end(self, data):
    #     new_node = Node(data)
    #     if not self.head:  # If the list is empty
    #         self.head = new_node
    #         self.head.next = self.head 
    #         self.tail = self.head  
    #     else:
    #         new_node.next = self.head  
    #         self.tail.next = new_node  
    #         self.tail = new_node
    # def delete_at_begin(self):
    #     if not self.head:  # If the list is empty
    #         print("Empty Circular Linked List. Nothing to delete.")
    #     elif self.head == self.tail:  # If there's only one node in the list
    #         self.head = None
    #         self.tail = None
    #     else:
    #         self.tail.next = self.head.next  # Update the next pointer of the tail node
    #         self.head = self.head.next 
    # def delete_at_end(self):
    #     if not self.head:  # If the list is empty
    #         print("Empty Circular Linked List. Nothing to delete.")
    #     elif self.head == self.tail:  # If there's only one node in the list
    #         self.head = None
    #         self.tail = None
    #     else:
    #         temp = self.head
    #         while temp.next != self.tail:  # Traverse the list until the second-to-last node
    #             temp = temp.next
    #         temp.next = self.head  # Update the next pointer of the second-to-last node to the head
    #         self.tail = temp
    def display(self):
        if self.head is None:
            print("Empty Circular Linked List")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print()


cll = CircularLinkedList()
cll.insert_at_begin(3)
cll.insert_at_end(7)
cll.delete_at_begin()
cll.delete_at_end()
cll.display() 
