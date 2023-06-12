import math

def fill(grid, number, xCurrent, yCurrent, xIncrement, yIncrement, count):
    global input
    for i in range(count):
        x = xCurrent + xIncrement * i
        y = yCurrent + yIncrement * i
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            break

        grid[xCurrent + xIncrement * i][yCurrent + yIncrement * i] = number + i

    return grid, number + count, xCurrent + xIncrement * count, yCurrent + yIncrement * count

def solve(input):
    length = math.ceil(math.sqrt(input)) + 1

    grid = []
    for i in range(length):
        grid.append([])
        for j in range(length):
            grid[i].append(0)

    xPos = length // 2
    yPos = length // 2

    number = 1
    increment = 1
    while(number < input):
        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, 1, 0, increment)

        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, 0, -1, increment)

        increment += 1
        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, -1, 0, increment)
        
        grid,number, xPos, yPos = fill(grid, number, xPos, yPos, 0, 1, increment)
        increment += 1

    xTarget = -1
    yTarget = -1
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == input:
                xTarget = x
                yTarget = y
                break
        if xTarget != -1:
            break

    xDiff = abs(xTarget - (length // 2))
    yDiff = abs(yTarget - (length // 2))

    print(xDiff + yDiff)

input = 347991
solve(input)