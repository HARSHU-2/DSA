# Zig Zap pattern
n = int(input("Rows: "))

for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()
