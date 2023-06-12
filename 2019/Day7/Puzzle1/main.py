import itertools

OPCODE_BREAK = 99
OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JNZ = 5
OPCODE_JZ = 6
OPCODE_LESS = 7
OPCODE_EQ = 8

PARMODE_POS = 0
PARMODE_IMME = 1

def getForPosition(ints, param):
    return int(ints[param])

def getImmediate(ints, param):
    return param

def getValue(ints, param, mode):
    if mode == PARMODE_POS:
        return getForPosition(ints, param)
    elif mode == PARMODE_IMME:
        return getImmediate(ints, param)

def solve(program, phase, inp):
    usedPhase = False
    usedInput = False

    ints = []
    with open(program) as f:
        for line in f:
            ints = line.split(",")

    i = 0
    while i < len(ints):
        code = str(ints[i]).zfill(5)
        op = int(code[-2:])

        if op == OPCODE_BREAK:
            break

        lhsMode = int(code[2])
        rhsMode = int(code[1])
        dstMode = int(code[0])
        inc = 0

        if op == OPCODE_ADD or op == OPCODE_MULT or op == OPCODE_LESS or op == OPCODE_EQ:
            inc = 4
            lhsPos = int(ints[i + 1])
            rhsPos = int(ints[i + 2])
            dst = int(ints[i + 3])
            lhs = getValue(ints, lhsPos, lhsMode)
            rhs = getValue(ints, rhsPos, rhsMode)

            if op == OPCODE_ADD:
                ints[dst] = lhs + rhs
            elif op == OPCODE_MULT:
                ints[dst] = lhs * rhs
            elif op == OPCODE_LESS:
                if lhs < rhs:
                    ints[dst] = 1
                else:
                    ints[dst] = 0
            elif op == OPCODE_EQ:
                if lhs == rhs:
                    ints[dst] = 1
                else:
                    ints[dst] = 0
        elif op == OPCODE_INPUT or op == OPCODE_OUTPUT:
            inc = 2
            pos = int(ints[i + 1])
            if op == OPCODE_INPUT:
                if not usedPhase:
                    value = phase
                    usedPhase = True
                elif not usedInput:
                    value = inp
                    usedInput = True
                else:
                    print("Extra input, something wrong?")
                    quit()
                ints[pos] = value
            elif op == OPCODE_OUTPUT:
                if lhsMode == PARMODE_POS:
                    return ints[pos]
                else:
                    return pos
        elif op == OPCODE_JNZ or op == OPCODE_JZ:
            inc = 3
            value = getValue(ints, int(ints[i + 1]), lhsMode)
            pointer = getValue(ints, int(ints[i + 2]), rhsMode)
            
            if op == OPCODE_JNZ:
                if not value == 0:
                    i = pointer
                    continue
            elif op == OPCODE_JZ:
                if value == 0:
                    i = pointer
                    continue

        i += inc

phases = [ 0, 1, 2, 3, 4 ]
perms = itertools.permutations(phases, 5)
largestOutput = 0
for perm in perms:
    inp = 0
    for phase in perm:
        inp = solve("../input.txt", phase, inp)
    largestOutput = max(inp, largestOutput)

print(largestOutput)