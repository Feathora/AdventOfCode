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

class Amplifier:
    ints = []
    i = 0
    usedPhase = False
    inputs = []
    halted = False
    finalOutput = 0

    def __init__(self, program, phase):
        self.phase = phase
        with open(program) as f:
            for line in f:
                self.ints = line.split(',')

    def process(self):
        i = self.i
        ints = self.ints
        while True:
            code = str(ints[i]).zfill(5)
            op = int(code[-2:])

            if op == OPCODE_BREAK:
                self.halted = True
                return -1

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
                    if not self.usedPhase:
                        value = self.phase
                        self.usedPhase = True
                    elif len(self.inputs) > 0:
                        value = self.inputs.pop(0)
                    else:
                        self.i = i
                        self.ints = ints
                        return -2
                    ints[pos] = value
                elif op == OPCODE_OUTPUT:
                    i += inc
                    self.i = i
                    self.ints = ints
                    if lhsMode == PARMODE_POS:
                        self.finalOutput = ints[pos]
                    else:
                        self.finalOutput = pos
                    return self.finalOutput
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

phases = [ 5, 6, 7, 8, 9 ]
perms = itertools.permutations(phases, 5)
largestOutput = 0
for perm in perms:
    amps = []
    for phase in perm:
        amps.append(Amplifier("../input.txt", phase))

    currentAmp = 0
    amps[currentAmp].inputs.append(0)
    while True:
        if not amps[currentAmp].halted:
            result = amps[currentAmp].process()
            if result == -2:
                currentAmp = (currentAmp + 1) % len(amps)
            elif result >= 0:
                amps[(currentAmp + 1) % len(amps)].inputs.append(result)
            elif result == -1:
                if currentAmp == len(amps) - 1:
                    largestOutput = max(largestOutput, amps[currentAmp].finalOutput)
                    print(amps[currentAmp].finalOutput)
                    break
                else:
                    currentAmp = (currentAmp + 1) % len(amps)
        else:
            currentAmp = (currentAmp + 1) % len(amps)

print(largestOutput)