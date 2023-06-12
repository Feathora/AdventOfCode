class Virus:
    x = 0
    y = 0
    xDir = 0
    yDir = -1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Move(self):
        self.x += self.xDir
        self.y += self.yDir

    def RotateLeft(self):
        if self.xDir != 0:
            self.yDir = -self.xDir
            self.xDir = 0
        else:
            self.xDir = self.yDir
            self.yDir = 0

    def RotateRight(self):
        if self.xDir != 0:
            self.yDir = self.xDir
            self.xDir = 0
        else:
            self.xDir = -self.yDir
            self.yDir = 0

def PrintGrid(grid):
    print("Grid:")
    for row in grid:
        print(row)

def solve(input):
    lines = input.splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))

    xPos = len(grid[0]) // 2
    yPos = len(grid) // 2

    virus = Virus(xPos, yPos)

    result = 0

    for i in range(10000):
        if grid[virus.y][virus.x] == '#':
            virus.RotateRight()
            grid[virus.y][virus.x] = '.'
        else:
            virus.RotateLeft()
            grid[virus.y][virus.x] = '#'
            result += 1

        virus.Move()

        if virus.x == -1:
            for y in range(len(grid)):
                grid[y] = [ '.' ] + grid[y]
            virus.x += 1
        elif virus.x == len(grid[0]):
            for y in range(len(grid)):
                grid[y].append('.')
        
        if virus.y == -1:
            grid = [['.' for j in range(len(grid[0]))]] + grid
            virus.y += 1
        elif virus.y == len(grid):
            grid.append(['.' for j in range(len(grid[0]))])

    print(result)

solve("""##.###.....##..#.####....
##...#.#.#..##.#....#.#..
...#..#.###.#.###.##.####
..##..###....#.##.#..##.#
###....#####..###.#..#..#
.....#.#...#..##..#.##...
.##.#.###.#.#...##.#.##.#
......######.###......###
#.....##.#....#...#......
....#..###.#.#.####.##.#.
.#.#.##...###.######.####
####......#...#...#..#.#.
###.##.##..##....#..##.#.
..#.###.##..#...#######..
...####.#...###..#..###.#
..#.#.......#.####.#.....
..##..####.######..##.###
..#..#..##...#.####....#.
.#..#.####.#..##..#..##..
......#####...#.##.#....#
###..#...#.#...#.#..#.#.#
.#.###.#....##..######.##
##.######.....##.#.#.#..#
..#..##.##..#.#..###.##..
#.##.##..##.#.###.......#""")