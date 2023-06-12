import sys

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    start = None
    end = None

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def left(self):
        return min(self.start.x, self.end.x)

    @property
    def right(self):
        return max(self.start.x, self.end.x)

    @property
    def top(self):
        return min(self.start.y, self.end.y)

    @property
    def bottom(self):
        return max(self.start.y, self.end.y)

    @property
    def length(self):
        return abs(self.end.x - self.start.x) + abs(self.end.y - self.start.y)


def solve(input):
    directions = []
    with open(input) as f:
        for line in f:
            directions.append(line.split(","))

    lines = [[], []]

    for i in range(len(directions)):
        x = 0
        y = 0
        for dir in directions[i]:
            amount = int(dir[1:])

            start = Point(x, y)

            if dir[0] == 'U':
                y -= amount
            elif dir[0] == 'D':
                y += amount
            elif dir[0] == 'L':
                x -= amount
            elif dir[0] == 'R':
                x += amount

            end = Point(x, y)

            line = Line(start, end)

            lines[i].append(line)

    lowestSteps = 9999999
    steps1 = 0

    for line1 in lines[0]:
        steps2 = 0
        for line2 in lines[1]:
            if (line1.start.x == line1.end.x and line2.start.x == line2.end.x) or (line1.start.y == line1.end.y and line2.start.y == line2.end.y):
                steps2 += line2.length
                continue

            if line1.start.x == line1.end.x:
                if (line1.left >= line2.left and line1.right <= line2.right) and (line2.top >= line1.top and line2.bottom <= line1.bottom):
                    x = line1.start.x
                    y = line2.start.y
                    steps1Bonus = abs(y - line1.start.y)
                    steps2Bonus = abs(x - line2.start.x)
                    combinedSteps = (steps1 + steps1Bonus) + (steps2 + steps2Bonus)
                    if combinedSteps > 0:
                        lowestSteps = min(lowestSteps, combinedSteps)
            else:
                if (line1.top >= line2.top and line1.bottom <= line2.bottom) and (line2.left >= line1.left and line2.right <= line1.right):
                    x = line2.start.x
                    y = line1.start.y
                    steps1Bonus = abs(x - line1.start.x)
                    steps2Bonus = abs(y - line2.start.y)
                    combinedSteps = (steps1 + steps1Bonus) + (steps2 + steps2Bonus)
                    if combinedSteps > 0:
                        lowestSteps = min(lowestSteps, combinedSteps)

            steps2 += line2.length

        steps1 += line1.length

    print(lowestSteps)

solve("../input.txt")