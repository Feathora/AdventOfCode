def solve(input):
    width = 25
    height = 6

    with open(input) as f:
        for line in f:
            depth = len(line) / (width * height)
            
            image = [[[0 for x in range(width)] for y in range(height)] for z in range(int(depth))]

            for i in range(len(line)):
                z = int(i / (width * height))
                y = int((i - (z * width * height)) / width)
                x = i % width

                image[z][y][x] = int(line[i])

            lowestZeroes = 999999999
            lowestLayer = -1
            for z in range(len(image)):
                layer = image[z]
                zeroes = 0
                for y in range(len(layer)):
                    for x in range(len(layer[y])):
                        if layer[y][x] == 0:
                            zeroes += 1
                if zeroes < lowestZeroes:
                    lowestZeroes = zeroes
                    lowestLayer = z

            ones = 0
            twos = 0
            for y in range(len(image[lowestLayer])):
                for x in range(len(image[lowestLayer][y])):
                    if image[lowestLayer][y][x] == 1:
                        ones += 1
                    elif image[lowestLayer][y][x] == 2:
                        twos += 1

            print(ones * twos)

solve("../input.txt")