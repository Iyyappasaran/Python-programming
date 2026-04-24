# Recreating Little Professor game using python
import random

def main():
    level = get_level()
    n = 0
    limit = 0
    count = 0
    while n < 10:
        n += 1
        while True:
            limit += 1
            try:
                if limit > 3:
                    print(f"{x} + {y} = {tot}")
                    limit = 0
                    break
                if limit == 1:
                    x, y, tot = generate_integer(level)
                ans = int(input(f"{x} + {y} = "))
                if ans == tot:
                    count += 1
                    limit = 0
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                    print("EEE")
    print(f"Score: {count}")
    
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1,2,3]:
                continue
            else:
                return n
        except ValueError:
            pass

def generate_integer(level):
    ranges = {1:9, 2:99, 3:999}
    max_val = ranges[level]
    a = random.randint(0,max_val)
    b = random.randint(0,max_val)
    return a, b, (a + b)

if __name__ == "__main__":
    main() 