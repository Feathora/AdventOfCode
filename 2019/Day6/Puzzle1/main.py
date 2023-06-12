def calcOrbits(planets, planet):
    orbits = 0
    while not planet == "COM":
        planet = planets.get(planet)
        orbits += 1

    return orbits

def solve(input):
    planets = {}
    with open(input) as f:
        for line in f:
            pair = line.split(')')
            planets[pair[1][0:3]] = pair[0]

    orbits = 0
    for planet in planets:
        orbits += calcOrbits(planets, planet)

    print(orbits)

solve("../input.txt")