def changeDirection(grid, x, y, xDir, yDir):
    if xDir != 0:
        if grid[y - 1][x] == '|':
            return 0, -1
        else:
            return 0, 1
    else:
        if grid[y][x - 1] == '-':
            return -1, 0
        else:
            return 1, 0

def solve(input):
    grid = input.splitlines()

    x = grid[0].index('|')
    y = 0

    xDir = 0
    yDir = 1

    result = ""

    while True:
        tile = grid[y][x]
        if tile != '+':

            if tile == ' ':
                break
            elif tile != '|' and tile != '-':
                result += tile
            
        else:
            xDir, yDir = changeDirection(grid, x, y, xDir, yDir)

        x += xDir
        y += yDir

    print(result)

with open ("../input.txt", "r") as inputFile:
    data = inputFile.read()
    solve(data)