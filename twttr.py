# Implement a program that prompts the user for string and outputs the strin with vowels removed
def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    result = ""
    for n in word:
        if n not in "AEIOUaeiou":
            result += n
    return f"{result}"

if __name__ == "__main__":
    main()
