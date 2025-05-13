class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(Stack)

    def pop(self):
        if len(self.stack) > 0:
            popped_item = self.stack.pop()
            print(Stack)
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty.")

    def display(self):
        print( self.stack)



my_stack = Stack()

while True:
        print("Menu:")
        print("Press 1 to Push")
        print("Press 2 to Pop")
        print("Press 3 to Peek")
        print("Press 4 to Display Stack")
        print("Press any other key to Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to push: ")
            my_stack.push(item)
        elif choice == "2":
            my_stack.pop()
        elif choice == "3":
            top_item = my_stack.peek()
            print(Stack)
        elif choice == "4":
            my_stack.display()
        else:
            print("Exiting the Stack program. Goodbye!")
            break
