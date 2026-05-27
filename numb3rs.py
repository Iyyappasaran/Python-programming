# Implementing a program to validate the IPv4 address(input) using regular expressions

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False
    parts = ip.split(".")
    for part in parts:
        part = int(part)
        if not 0 <= part <= 255:
            return False
    return True
        
    
if __name__ == "__main__":
    main()