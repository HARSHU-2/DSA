# Move zeros to the end
n = int(input("Enter Numbers:"))
arr = []

for i in range(n):
    arr.append(int(input("Enter Elements:")))

result = []
zero = 0

for i in arr:
    if i == 0:
        zero += 1
    else:
        result.append(i)

for i in range(zero):
    result.append(0)

print("Orginal:", arr)
print("Result:", result)
