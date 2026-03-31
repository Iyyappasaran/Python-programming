# Implementing a program that prompts user for answer if True "Yes" else "No"
text = input("What is the Answer to the Great Question of Life, Universe and Eveerything? ").lower().strip()
match text:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")