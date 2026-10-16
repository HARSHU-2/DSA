# Create a Doubly Linear Linked List
# Create Linked List
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

# Insert node at a specific position
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while (p != pos-1):
                temp = temp.next
                p += 1
            if temp.next:
                temp.next.prev = new_node
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node

# Delete node
    def delete(self, value):
        temp = self.head
        prev = None
        if temp.data == value:
            self.head = self.head.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head
        else:
            while (temp.data != value and temp):
                prev = temp
                temp = temp.next
                if temp == self.head:
                    print("Value is not present in the list")
                    return
            prev.next = temp.next
            temp = None

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


list1 = DLL()
n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()

print(("After insertion"))
list1.insert(Node(58), 1)
list1.insert(Node(50), 6)
list1.print()

# list1.delete(10)
# list1.print()
