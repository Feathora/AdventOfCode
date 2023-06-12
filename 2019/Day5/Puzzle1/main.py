def solve(input):
    ints = []
    with open(input) as f:
        for line in f:
            ints = line.split(",")

    i = 0
    while i < len(ints):
        code = str(ints[i]).zfill(5)
        op = int(code[-2:])

        if op == 99:
            break

        lhsMode = int(code[2])
        rhsMode = int(code[1])
        dstMode = int(code[0])
        inc = 0

        if op == 1 or op == 2:
            inc = 4
            lhsPos = int(ints[i + 1])
            rhsPos = int(ints[i + 2])
            dst = int(ints[i + 3])
            if lhsMode == 0:
                lhs = int(ints[lhsPos])
            else:
                lhs = lhsPos
            if rhsMode == 0:
                rhs = int(ints[rhsPos])
            else:
                rhs = rhsPos

            if op == 1:
                ints[dst] = lhs + rhs
            elif op == 2:
                ints[dst] = lhs * rhs
        elif op == 3 or op == 4:
            inc = 2
            pos = int(ints[i + 1])
            if op == 3:
                s = 1
                value = int(s)
                ints[pos] = value
            elif op == 4:
                if lhsMode == 0:
                    print(ints[pos])
                else:
                    print(pos)

        i += inc

solve("../input.txt")