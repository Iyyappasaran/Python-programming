# Implement a program that prompts user for a fraction and catch exceptions and errors then print the fuel in tank
def main():
        fuel = input("Fraction: ")
        print(f"{gauge(convert(fuel))}")

def convert(n):
        x , y = n.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
             raise ZeroDivisionError
        if x > y:
             raise ValueError
    
        percent = round((x/y)*100)
        return percent

def gauge(z):
    if z <= 1:
        return "E"
    elif z >= 99:
        return "F"
    else:
        return f"{z}%"

if __name__ == "__main__":
    main()
