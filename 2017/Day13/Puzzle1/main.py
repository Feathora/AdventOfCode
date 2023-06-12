def solve(input):
    lines = input.splitlines()

    layers = {}

    finalLayer = 0

    for line in lines:
        values = line.split(': ')

        layer = int(values[0])
        depth = int(values[1])
        layers[layer] = { "depth": depth, "scanner": 0, "direction": 1 }

        finalLayer = layer

    severity = -1
    position = -1

    delayTime = -1

    while severity != 0:
        position = -1
        severity = 0
        delayTime += 1
        time = 0

        for layer in layers:
            layers[layer]["scanner"] = 0
            layers[layer]["direction"] = 1

        while position <= finalLayer:
            if time < delayTime:
                time += 1
            else:
                position += 1

                if position in layers:
                    if layers[position]["scanner"] == 0:
                        severity += position * layers[position]["depth"]

            for layer in layers:
                layers[layer]["scanner"] += layers[layer]["direction"]
                if layers[layer]["scanner"] == layers[layer]["depth"] - 1 or layers[layer]["scanner"] == 0:
                    layers[layer]["direction"] *= -1

        if severity == 0:
            break

    print(delayTime)



solve("""0: 3
1: 2
2: 4
4: 6
6: 5
8: 8
10: 6
12: 4
14: 8
16: 6
18: 8
20: 8
22: 6
24: 8
26: 9
28: 12
30: 8
32: 14
34: 10
36: 12
38: 12
40: 10
42: 12
44: 12
46: 12
48: 12
50: 14
52: 12
54: 14
56: 12
60: 14
62: 12
64: 14
66: 14
68: 14
70: 14
72: 14
74: 14
78: 26
80: 18
82: 17
86: 18
88: 14
96: 18""")