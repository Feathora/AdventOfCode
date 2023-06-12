def addFuel(fuel):
    extraFuel = (int)(fuel / 3) - 2
    if extraFuel > 0:
        extraFuel += addFuel(extraFuel)

    return max(extraFuel, 0)

def solve(input):
    n = 0
    with open(input) as f:
        for line in f:
            fuel = (int)(int(line) / 3) - 2
            fuel += addFuel(fuel)
            n += fuel

    print(n)

solve("../input.txt")