# Q. 2 Write a program to perform the following operations on a Linear Queue
# 1. Enqueue an element into the queue
# 2. Dequeue an element from the queue
# 3. Display
# 4. Reverse the queue using stack
# 5. Merge two queues into one.
# 6. Check if two queues are identical
queue = [10, 20, 30, 40]
queue2 = [50, 60, 70]

print("Original Queue 1:", queue)
print("Original Queue 2:", queue2)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        queue.append(x)
        print("After Enqueue:", queue)

    elif ch == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Dequeued Element:", queue.pop(0))
            print("After Dequeue:", queue)

    elif ch == 3:
        print("Queue:", queue)

    elif ch == 4:
        stack = []

        while queue:
            stack.append(queue.pop(0))

        while stack:
            queue.append(stack.pop())

        print("Reversed Queue:", queue)

    elif ch == 5:
        merged = queue + queue2
        print("Queue 1:", queue)
        print("Queue 2:", queue2)
        print("Merged Queue:", merged)

    elif ch == 6:
        if queue == queue2:
            print("Both Queues are Identical")
        else:
            print("Both Queues are Not Identical")

    elif ch == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
