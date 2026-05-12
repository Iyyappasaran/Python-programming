# Reformatting before.csv into after.csv file

import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as infile, open(sys.argv[2], "w",newline = "") as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            next(reader)
            writer.writerow(["last", "first", "house"])
            for row in reader:
                name = row[0]
                last, first = name.split(",")
                house = row[1]
                writer.writerow([last.strip(), first.strip(), house.strip()])
    except FileNotFoundError:
        sys.exit("File does not exist")
