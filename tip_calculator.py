# Creating tip calculator: Calculating tip using bill amount and tip percent from user
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars*percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(x):
    x = x.replace("$","")
    return float(x)
def percent_to_float(y):
    y = y.replace("%","")
    return float(y)/100

main()