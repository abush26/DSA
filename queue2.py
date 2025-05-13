#  Array Representation 
class Queue:
    def __init__(self, items=[]):
        self.queue = items

    def enqueue(self, item):
        self.queue.append(item)
        print(Queue)

    def dequeue(self):
        if len(self.queue) > 0:
            dequeued_item = self.queue.pop(0)
            print(Queue)
        else:
            print("Queue is empty. Cannot dequeue.")

    def size(self):
        return len(self.queue)

    def display(self):
        print(Queue)


# Menu for interacting with the Queue
my_queue = Queue()

while True:
    print("Menu:")
    print("Press 1 to Enqueue")
    print("Press 2 to Dequeue")
    print("Press 3 to Display Queue")
    print("Press any other key to Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            item = input("Enter the element to enqueue: ")
            my_queue.enqueue(item)
    elif choice == "2":
            my_queue.dequeue()
    elif choice == "3":
            my_queue.display()
    else:
            print("Exiting the Queue program. Goodbye!")
            break
