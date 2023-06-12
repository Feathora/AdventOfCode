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

    programs = [{ "p": 0, "queue": [], "position": 0, "terminated": False }, { "p": 1, "queue": [], "position": 0, "terminated": False }]

    result = 0

    while True:
        deadlock = 0

        for i in range(len(programs)):
            program = programs[i]

            position = program["position"]

            instructions = lines[position].split(' ')

            instruction = instructions[0]
            if not isInt(instructions[1]):
                checkRegister(program, instructions[1])

            if instruction == "snd":
                programs[(i + 1) % len(programs)]["queue"].append(getValue(program, instructions[1]))
            elif instruction == "set":
                l = instructions[1]
                r = instructions[2]
                setRegister(program, l, r)
            elif instruction == "add":
                addRegister(program, instructions[1], instructions[2])
            elif instruction == "mul":
                mulRegister(program, instructions[1], instructions[2])
            elif instruction == "mod":
                modRegister(program, instructions[1], instructions[2])
            elif instruction == "rcv":
                queue = programs[i]["queue"]
                if len(queue) == 0:
                    deadlock += 1
                    continue
                setRegister(program, instructions[1], queue[0])
                programs[i]["queue"] = queue[1:]
                if i == 0:
                    result += 1
            elif instruction == "jgz":
                if getValue(program, instructions[1]) > 0:
                    position += getValue(program, instructions[2])
                    program["position"] = position
                    continue

            position += 1
            program["position"] = position

        if deadlock == len(programs):
            break

    print(result)

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