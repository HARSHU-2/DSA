# Search an Element.
n = int(input("Enter Number:"))
arr = []

for i in range(n):
    arr.append(int(input("Enter element:")))

search = int(input("Enter number to search:"))

if search in arr:
    print("Found at position", arr.index(search) + 1)
else:
    print("Not Found")
