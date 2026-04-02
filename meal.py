# Implement a program that prompts  the user for time and outputs meal time
def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")
    
def convert(text):
    x , y = text.split(":")
    x = float(x)
    y = float(y)
    return x + (y / 60)

main()