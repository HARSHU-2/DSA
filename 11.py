# reverse words
s = input("Enter sentence: ")

words = s.split()

for word in words:
    print(word[::-1], end=" ")
