# Count even odd
n = int(input("Enter Numbers: "))
arr = []

for i in range(n):
    num = int(input("Enter Elements:"))
    arr.append(num)

odd = 0
even = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Number =", even)
print("Odd Number =", odd)
