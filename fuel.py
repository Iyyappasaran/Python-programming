# Implement a program that prompts user for a fraction and catch exceptions and errors then print the fuel in tank
def main():
    fuel = error()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{round(fuel)}%")

def error():
    while True:
        try:
            x , y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            if x > y or y == 0:
                continue
            return (x/y)*100
        except (ValueError,ZeroDivisionError):
            pass

main()