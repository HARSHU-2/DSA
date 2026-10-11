# Find smallest and largest element
n = int(input("Enter the number of elements:"))
arr = []

for i in range(n):
    num = int(input("Enter Elements:"))
    arr.append(num)

arr.sort()

print("Smallest  = ", arr[0])
print("Second Smallest = ", arr[1])
print("Largest = ", arr[n - 1])
print("Second Largest = ", arr[n - 2])
