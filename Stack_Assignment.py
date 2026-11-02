# Q. 1 Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display
# 4. Reverse String using Stack
# 5. Reverse Stack using another Stack
stack = [10, 20, 30, 40]

print("Original Stack:", stack)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        stack.append(x)
        print("After Push:", stack)

    elif ch == 2:
        if len(stack) == 0:
            print("Stack is Empty")
        else:
            print("Popped Element:", stack.pop())
            print("After Pop:", stack)

    elif ch == 3:
        print("Current Stack:", stack)

    elif ch == 4:
        s = input("Enter string: ")
        temp = []

        for i in s:
            temp.append(i)

        rev = ""
        while temp:
            rev += temp.pop()

        print("Original String:", s)
        print("Reversed String:", rev)

    elif ch == 5:
        temp = []

        while stack:
            temp.append(stack.pop())

        stack = temp
        print("After Reverse Stack:", stack)

    elif ch == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
