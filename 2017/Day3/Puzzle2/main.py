import math

solved = False

def fill(grid, number, xCurrent, yCurrent, xIncrement, yIncrement, count):
    global input, solved
    for i in range(count):
        x = xCurrent + xIncrement * i
        y = yCurrent + yIncrement * i
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            break

        sum = 0
        for xSum in range(max(x - 1, 0), min(x + 2, len(grid))):
            for ySum in range(max(y - 1, 0), min(y + 2, len(grid[xSum]))):
                sum += grid[xSum][ySum]

        grid[x][y] = sum

        if not solved and sum > input:
            print(sum)
            solved = True

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

    grid[xPos][yPos] = 1

    number = 1
    increment = 1
    while(number < length * length):
        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, 1, 0, increment)

        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, 0, -1, increment)
        increment += 1
        
        grid, number, xPos, yPos = fill(grid, number, xPos, yPos, -1, 0, increment)
        
        grid,number, xPos, yPos = fill(grid, number, xPos, yPos, 0, 1, increment)
        increment += 1

    # for x in range(len(grid)):
    #     print(grid[x])

input = 347991
#input = 100
solve(input)