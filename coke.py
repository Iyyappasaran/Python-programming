# Implement a program that calculates the amount due each time when inserted a coin for coke.
due = 50
while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        due -= coin
owe = abs(due)
print("Change Owed:",owe)