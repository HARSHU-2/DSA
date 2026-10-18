# Ass1: Create a Singly Linear Linked List
# Create Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

# Traverse and print node values
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Insert node at a specific position
    def insert(self, node, pos):
        if pos == 1:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for i in range(pos - 2):
                temp = temp.next
            node.next = temp.next
            temp.next = node

# Find middle node and delete the node
    def findmid_del(self):
        temp = temp1 = self.head
        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp = temp1.next.next
        print("Middle Node: ", temp.data)
        prev.next = temp.next
        temp = None

# Delete node
    def delfirst_last(self):
        temp1 = self.head
        temp1 = None
        prev = None
        temp = self.head = self.head.next
        while (temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None

# Reverse list
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev

# Calculate the sum of every two consecutive node values
    def sum(self):
        temp = self.head
        while (temp.next):
            print(temp.data, "+", temp.next.data, "=", temp.data + temp.next.data)
            temp = temp.next


list1 = SLL()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Linked list:")
list1.print()

list1.insert(Node(15), 2)
print("After insertion:")
list1.print()

list1.delfirst_last()
print("After deletion:")
list1.print()

list1.reverse()
print("After reverse:")
list1.print()

print("Sum of every two consecutive node values:")
list1.sum()

list1.findmid_del()
list1.print()
