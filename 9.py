# Write a program to count vowels, consonants, digits and special
# characters in a given string.
s = input("Enter String: ")

v = c = d = sp = 0

for ch in s:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special:", sp)
