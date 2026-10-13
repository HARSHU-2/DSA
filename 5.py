# Reverse array
n = int(input("Enter Number:"))
arr = []

for i in range(n):
    arr.append(int(input("Enter element:")))

reverse = arr[::-1]

print("Orignal:", arr)
print("Reverse:", reverse)
