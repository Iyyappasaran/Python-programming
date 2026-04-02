# Implement a program that prompts the user for an arithmetic expression and then outputs the value
text = input("Expression: ")
x , y , z = text.split()
x = float(x)
z = float(z)
match y:
    case "+":
        print(f"{(x + z):.1f}")
    case "-":
        print(f"{(x - z):.1f}")
    case "*":
        print(f"{(x * z):.1f}")
    case "/":
        print(f"{(x / z):.1f}")
