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

def solve(input):
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

    print(output)

solve("34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167")