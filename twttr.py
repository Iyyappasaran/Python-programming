# Implement a program that prompts the user for string and outputs the strin with vowels removed
text = input("Input: ")
result = ""
for n in text:
    if n not in "AEIOUaeiou":
        result += n
print("Output:",result)