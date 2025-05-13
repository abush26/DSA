class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print("Stack is empty.")

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage of the Stack class
if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Stack:")
    my_stack.display()

    popped_item = my_stack.pop()
    print(f"Popped item: {popped_item}")

    print("Updated Stack:")
    my_stack.display()

    top_item = my_stack.peek()
    print(f"Top item: {top_item}")
