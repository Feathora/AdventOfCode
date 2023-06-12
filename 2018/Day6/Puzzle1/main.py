import re

def solve(input):
    xMax = 0
    yMax = 0

    coords = []

    with open(input) as f:
        for line in f:
            matches = re.findall(r'[0-9]+', line)
            x = int(matches[0])
            y = int(matches[1])
            coords.append({ 'x': x, 'y': y })

            xMax = max(x, xMax)
            yMax = max(y, yMax)

    grid = [[{} for x in range(xMax + 1)] for y in range(yMax + 1)]

    for coord in coords:
        grid[coord['x']][coord['y']] = coord

solve("../input.txt")