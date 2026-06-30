# Coverting the input from 12 hour format to 24 hour format using regular expressions

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",s,re.IGNORECASE):
        hr1,min1,abr1,hr2,min2,abr2 = matches.groups()
    else:
        raise ValueError
    
    hr1 = int(hr1)
    hr2 = int(hr2)
    min1 = int(min1) if min1 else 0
    min2 = int(min2) if min2 else 0

    if not (1 <= hr1 <= 12 and 1 <= hr2 <= 12):
        raise ValueError
    if not (0 <= min1 <= 59 and 0 <= min2 <= 59):
        raise ValueError
    
    if abr1.upper() == "AM":
        if hr1 == 12:
            hr1 = 0
    else:
        if hr1 != 12:
            hr1 += 12
    
    if abr2.upper() == "AM":
        if hr2 == 12:
            hr2 = 0
    else:
        if hr2 != 12:
            hr2 += 12

    return f"{hr1:02}:{min1:02} to {hr2:02}:{min2:02}"

if __name__ == "__main__":
    main()