# Longest shortest word
s = input("Enter sentence: ")

words = s.split()

longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word

print("Longest:", longest)
print("Shortest:", shortest)
