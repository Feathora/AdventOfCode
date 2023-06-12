def solve(input, noun, verb):
    ints = []
    with open(input) as f:
        for line in f:
            ints = line.split(",")

    ints[1] = noun
    ints[2] = verb

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

    return ints[0]

for noun in range(100):
    for verb in range(100):
        solution = solve("../input.txt", noun, verb)

        if solution == 19690720:
            print(100 * noun + verb)