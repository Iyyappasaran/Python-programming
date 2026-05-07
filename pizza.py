# Converting the values in a .csv file into ASCII art

import sys
from tabulate import tabulate

table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            header = file.readline()
            for line in file:
                line = line.strip().split(",")
                table.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

print(tabulate(table,headers=header.strip().split(","),tablefmt="grid"))