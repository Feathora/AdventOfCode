def solve(input):
    n = 0
    with open(input) as f:
        for line in f:
            n += (int)(int(line) / 3) - 2

    print(n)

solve("../input.txt")