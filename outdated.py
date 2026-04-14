# Get input from user of date in outdated format and output it in international standard format
months = {"January": 1,
         "February": 2,
         "March": 3,
         "April": 4,
         "May": 5,
         "June": 6,
         "July": 7,
         "August": 8,
         "September": 9,
         "October": 10,
         "November": 11,
         "December": 12
}
while True:
    try:
        month, date, year = input("Date: ").replace("/"," ").replace(",","").split()
        if month in months:
            month = months[month]
        else:
            month = int(month)
        date = int(date)
        year = int(year)
        if date < 1 or date > 31:
            continue
        break
    except ValueError:
        pass

print(f"Date: {year}-{month:02}-{date:02}")