# Implement a program thet prompts the user for names the bid aideu to those names and output after modification.
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
adieu = "Adieu, adieu, to"
if len(names) == 1:
    print(f"{adieu} {names[0]}")
elif len(names) == 2:
    print(f"{adieu} {names[0]} and {names[1]}")
else:
    print(f"{adieu} {', '.join(names[:-1])}, and {names[-1]}")