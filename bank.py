# Implement a program that prompts user for greeting and do operation with conditionals
text = input("Greeting: ").strip().lower()
if text.startswith("hello"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")