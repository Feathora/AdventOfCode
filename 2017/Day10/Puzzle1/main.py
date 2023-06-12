def solve(input):
    lengths = input.split(',')

    hash = list(range(256))
    position = 0
    skip = 0

    for length in lengths:
        l = int(length)

        for i in range(l // 2):
            left = (position + i) % len(hash)
            right = (position + l - i - 1) % len(hash)

            temp = hash[left]
            hash[left] = hash[right]
            hash[right] = temp

        position = (position + l + skip) % len(hash)
        skip += 1

    print(hash[0] * hash[1])

solve("34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167")