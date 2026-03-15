# Finding energy using Einstein's formula and mass input
def main():
    mass = int(input())
    print(energy(mass))

def energy(value):
    C = 300000000
    return value*C*C

main()