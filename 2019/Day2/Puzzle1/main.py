def solve(input):
    ints = []
    with open(input) as f:
        for line in f:
            ints = line.split(",")

    ints[1] = 12
    ints[2] = 2

    for i in range(0, len(ints), 4):
        op = int(ints[i])

        if op == 99:
            break

        lhs = int(ints[i + 1])
        rhs = int(ints[i + 2])
        dst = int(ints[i + 3])

        if op == 1:
            ints[dst] = int(ints[lhs]) + int(ints[rhs])
        elif op == 2:
            ints[dst] = int(ints[lhs]) * int(ints[rhs])

    print(ints[0])

solve("../input.txt")