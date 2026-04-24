# Creating a Guessing game 
import random

# Instructions
print("Level Instructions:")
print("Level 1: 1 - 20, limit = 3")
print("Level 2: 1 - 40, limit = 4")
print("Level 3: 1 - 60, limit = 5")
print("Level 4: 1 - 80, limit = 6")
print("Level 5: 1 - 100, limit = 7\n")

# Getting the value n from user
while True:
    try:
        level = int(input("Level: "))
        if 5 >= level > 0:
            break
    except ValueError:
        pass

# Choosing number:
ranges = {1:(20,3), 2:(40,4), 3:(60,5), 4:(80,6), 5:(100,7)}
max_val, limit = ranges[level]
number = random.randint(1,max_val)


# Getting the guess value from user
n = 0
while True:
    try:
        print(f"Attempts left: {limit-n}")
        n += 1
        if n > limit:
            print("\nOut of limit")
            print("You lose")
            break
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            print("You won")
            break
    except ValueError:
        pass
