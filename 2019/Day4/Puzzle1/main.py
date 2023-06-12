def sameAdjecent(input):
    for i in range(len(input) - 1):
        n = input[i]
        n1 = input[i + 1]
        if n == n1:
            return True

    return False

def neverDecrease(input):
    for i in range(len(input) - 1):
        n = int(input[i])
        n1 = int(input[i + 1])
        if n > n1:
            return False

    return True

def solve(input):
    low = 0
    high = 0
    with open(input) as f:
        for line in f:
            r = line.split('-')
            low = int(r[0])
            high = int(r[1])

    counter = 0
    for i in range(low, high):
        if not sameAdjecent(str(i)):
            continue
        if not neverDecrease(str(i)):
            continue
        counter += 1

    print(counter)

solve("../input.txt")