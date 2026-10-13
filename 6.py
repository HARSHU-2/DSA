# Remove duplicates
n = int(input("Enter Number:"))
arr = []

for i in range(n):
    arr.append(int(input("Enter Elements:")))

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Original:", arr)
print("Unique:", unique)
