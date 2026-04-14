# Get grocery items as input from user and make a list
items = {}
while True:
    try:
        item = input().strip().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        break
for item in sorted(items):
    print(items[item],item)