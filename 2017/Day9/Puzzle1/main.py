def solve(input):
    result = 0

    groupLevel = 0
    ignoreNext = False
    garbage = False

    for c in input:
        if ignoreNext:
            ignoreNext = False
        elif garbage:
            if c == '>':
                garbage = False
            elif c == '!':
                ignoreNext = True
        elif c == '{':
            groupLevel += 1
        elif c == '}':
            result += groupLevel
            groupLevel -= 1
        elif c == '<':
            garbage = True

    print(result)

with open ("input.txt", "r") as inputFile:
    data = inputFile.read()
    solve(data)