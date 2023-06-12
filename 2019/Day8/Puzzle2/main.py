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

            finalImage = [[2 for x in range(width)] for y in range(height)]
            for z in range(len(image)):
                for y in range(len(image[z])):
                    for x in range(len(image[z][y])):
                        if finalImage[y][x] != 2:
                            continue

                        finalImage[y][x] = image[z][y][x]

            imageStr = ""
            for y in range(len(finalImage)):
                for x in range(len(finalImage[y])):
                    if finalImage[y][x] == 1:
                        imageStr += "1"
                    else:
                         imageStr += " "
                imageStr += "\n"

            print(imageStr)

solve("../input.txt")