def solve(input):
    buffer = [0]
    position = 0

    zeroPos = 0
    nextValue = -1
    for i in range(50000000):
        position = (position + input) % (i + 1)
        if position == zeroPos:
            nextValue = i + 1
        position += 1

    print(nextValue)

solve(304)