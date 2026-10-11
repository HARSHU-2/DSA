# write a program to accept N integers into an array and calculate and
# display sum of all the elements.
n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter Element:"))
    arr.append(num)

sum = 0

for i in arr:
    sum += i
print("Sum =", sum)
