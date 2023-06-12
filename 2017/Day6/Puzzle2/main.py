def findMax(input):
    highestIndex = -1
    highest = -1
    for i in range(len(input)):
        if input[i] > highest:
            highestIndex = i
            highest = input[i]

    return highestIndex

def listEquals(lhs, rhs):
    result = True
    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            result = False
            break
    return result

def solve(input):
    words = input.split('\t')

    containers = []
    for word in words:
        containers.append(int(word))

    archive = []

    result = 0

    while(True):
        containerIndex = findMax(containers)
        num = containers[containerIndex]

        containers[containerIndex] = 0

        for i in range(num):
            containers[(containerIndex + 1 + i) % len(containers)] += 1

        config = []
        for c in containers:
            config.append(c)

        done = False
        for i in range(len(archive)):
            entry = archive[i]
            if listEquals(entry, config):
                done = True
                result = len(archive) - i
                break

        if done:
            break
        else:
            archive.append(config)

    print(result)

solve("11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11")