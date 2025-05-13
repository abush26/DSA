 
# Menu 
queue = [1,2,3,4]

while True:
    print("Press 1 to enqueue")
    print("Press 2 to dequeue")
    print("Press 3 to display")
    print("Press any other key to exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
       
        element = input("Enter the element to enqueue: ")
        queue.append(element)
        print(queue)
    elif choice == "2":
       
        if len(queue) > 0:
            dequeued_element = queue.pop(0)
            print(queue)
        else:
            print("Queue is empty. Cannot dequeue.")
    elif choice == "3":
       
        print( queue)
    else:
       
        print("Exiting the queue program. Goodbye!")
        break