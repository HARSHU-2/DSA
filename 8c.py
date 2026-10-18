# Print hollow diamond
n = int(input("Rows: "))

for i in range(1, n + 1):
    print(" " * (n-i), end="")
    print("*" if i == 1 else "*" + " " * (2*i-3) + "*")

for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    print("*" if i == 1 else "*" + " " * (2*i-3) + "*")
