def round(hash, lengths, position, skip):
    for length in lengths:

        for i in range(length // 2):
            left = (position + i) % len(hash)
            right = (position + length - i - 1) % len(hash)

            temp = hash[left]
            hash[left] = hash[right]
            hash[right] = temp

        position = (position + length + skip) % len(hash)
        skip += 1

    return hash, position, skip

def createHash(input):
    lengths = []
    for c in input:
        lengths.append(ord(c))

    lengths += [17, 31, 73, 47, 23]

    hash = list(range(256))
    position = 0
    skip = 0

    for i in range(64):
        hash, position, skip = round(hash, lengths, position, skip)

    result = []
    for i in range(0, len(hash), 16):
        char = 0
        for x in range(i, i + 16):
            char ^= hash[x]

        result.append(char)

    output = ""
    for i in result:
        output += "%0.2x" % i

    return output

def check(grid, used, x, y):
    used[y][x] = True

    if x > 0 and not used[y][x - 1] and grid[y][x - 1] == 1:
        check(grid, used, x - 1, y)

    if y > 0 and not used[y - 1][x] and grid[y - 1][x] == 1:
        check(grid, used, x, y - 1)

    if x < 127 and not used[y][x + 1] and grid[y][x + 1] == 1:
        check(grid, used, x + 1, y)

    if y < 127 and not used[y + 1][x] and grid[y + 1][x] == 1:
        check(grid, used, x, y + 1)

def solve(input):
    grid = [[0 for i in range(128)] for j in range(128)]

    for y in range(128):
        key = input + "-" + str(y)
        value = createHash(key)

        for i in range(len(value)):
            c = value[i]
            bits = int(c, 16)

            for b in range(4):
                x = i * 4 + (3 - b)
                bit = 1 << b
                if (bit & bits) == bit:
                    grid[y][x] = 1

    regions = 0
    used = [[False for i in range(128)] for j in range(128)]
    for y in range(128):
        for x in range(128):
            if used[y][x]:
                continue
            if grid[y][x] == 0:
                used[y][x] = True
                continue

            regions += 1
            check(grid, used, x, y)

    print(regions)
        
    

solve("oundnydw")