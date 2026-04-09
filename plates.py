# Implement a program that prompts the user for vanity plate if it meets all requirements print "valid" else "Invalid"
def main():
    text = input("Plate: ")
    if is_valid(text):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start(s) and limit(s) and number(s) and special(s):
        return True
    else:
        return False
    
def start(x):
    if len(x) < 2:
        return False
    return x[0].isalpha and x[1].isalpha

def limit(y):
    if 2 <= len(y) <= 6:
        return True
    else:
        return False

def number(z):
    number_start = False
    for i in z:
        if not number_start:
            if i.isdigit():
                if i == "0":
                    return False
                number_start = True
        else:
            if not i.isdigit():
                return False
    return True
            
def special(w):
    return w.isalnum()
        
main()