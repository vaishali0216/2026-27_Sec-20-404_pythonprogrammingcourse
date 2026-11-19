str1 = input("Enter a string: ")

rev = str1[::-1]

print("Original String:", str1)
print("Reversed String:", rev)

if str1 == rev:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")