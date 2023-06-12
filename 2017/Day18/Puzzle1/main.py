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

def addRegister(registers, register, value):
    registers[register] += getValue(registers, value)

def mulRegister(registers, register, value):
    registers[register] *= getValue(registers, value)

def modRegister(registers, register, value):
    registers[register] %= getValue(registers, value)

def solve(input):
    lines = input.splitlines()

    registers = {}

    sound = 0

    position = 0
    while position >= 0 and position < len(lines):
        instructions = lines[position].split(' ')

        instruction = instructions[0]
        if not isInt(instructions[1]):
            checkRegister(registers, instructions[1])

        if instruction == "snd":
            sound = getValue(registers, instructions[1])
        elif instruction == "set":
            l = instructions[1]
            r = instructions[2]
            setRegister(registers, l, r)
        elif instruction == "add":
            addRegister(registers, instructions[1], instructions[2])
        elif instruction == "mul":
            mulRegister(registers, instructions[1], instructions[2])
        elif instruction == "mod":
            modRegister(registers, instructions[1], instructions[2])
        elif instruction == "rcv":
            if sound != 0:
                print(sound)
                break
        elif instruction == "jgz":
            if getValue(registers, instructions[1]) > 0:
                position += getValue(registers, instructions[2])
                continue

        position += 1
            

solve("""set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 735
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19""")