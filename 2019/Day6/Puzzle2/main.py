def solve(input):
    planets = {}
    with open(input) as f:
        for line in f:
            pair = line.split(')')
            planets[pair[1][0:3]] = pair[0]

    graph = { 'COM': { 'V9S': 1 }}
    for planet in planets:
        node = {}
        orbitsAround = planets.get(planet)
        node[orbitsAround] = 1

        for p in planets:
            if planets.get(p) == planet:
                inOrbit = p
                node[inOrbit] = 1

        graph[planet] = node

    initial = 'YOU'
    path = {}
    adj_node = {}
    queue = []
    
    for node in graph:
        path[node] = float("inf")
        adj_node[node] = None
        queue.append(node)

    path[initial] = 0

    while queue:
        key_min = queue[0]
        min_val = path[key_min]
        for n in range(1, len(queue)):
            if path[queue[n]] < min_val:
                key_min = queue[n]
                min_val = path[key_min]
        cur = key_min
        queue.remove(cur)

        for i in graph[cur]:
            alternate = graph[cur][i] + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = cur

    x = 'SAN'
    steps = 0
    while True:
        x = adj_node[x]
        if x is None:
            print(steps - 2)
            break
        steps += 1

solve("../input.txt")