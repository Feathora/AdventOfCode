def isInt(value):
    try:
        int(value)
        return True
    except:
        return False

def checkRegister(registers, register):
    if not register in registers:
        registers[register] = 0

def getRegister(registers, register):
    checkRegister(registers, register)

    return registers[register]

def getValue(registers, value):
    if not isInt(value):
        return getRegister(registers, value)
    else:
        return int(value)

def setRegister(registers, register, value):
    registers[register] = getValue(registers, value)

def subRegister(registers, register, value):
    registers[register] -= getValue(registers, value)

def mulRegister(registers, register, value):
    registers[register] *= getValue(registers, value)

def solve(input):
    lines = input.splitlines()

    registers = { 'a': 1 }

    position = 0
    result = 0
    while position >= 0 and position < len(lines):
        instructions = lines[position].split(' ')

        jump = 1

        instruction = instructions[0]
        if not isInt(instructions[1]):
            checkRegister(registers, instructions[1])

        if instruction == "set":
            l = instructions[1]
            r = instructions[2]
            setRegister(registers, l, r)
        elif instruction == "sub":
            subRegister(registers, instructions[1], instructions[2])
        elif instruction == "mul":
            mulRegister(registers, instructions[1], instructions[2])
            result += 1
        elif instruction == "jnz":
            if getValue(registers, instructions[1]) != 0:
                jump = getValue(registers, instructions[2])

        position += jump

    print(registers['h'])


solve("""set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23""")