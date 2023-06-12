class Port:
    def __init__(self, value):
        self.value = value
        self.used = False

class Component:
    def __init__(self, line, index):
        self.ports = []
        self.index = index
        ps = line.split('/')
        for p in ps:
            self.ports.append(Port(int(p)))

    def HasFreePort(self, value):
        for p in self.ports:
            if p.value == value and not p.used:
                p.used = True
                return True

        return False

    def GetFreePort(self):
        for p in self.ports:
            if not p.used:
                return p.value

        return -1

    def Used(self):
        for p in self.ports:
            if p.used:
                return True

        return False

    def Use(self):
        for p in self.ports:
            p.used = True

    def Reset(self):
        for p in self.ports:
            p.used = False

def FindNextComponent(components, portValue, start):
    for i in range(start, len(components)):
        if not components[i].Used():
            free = components[i].HasFreePort(portValue)
            if free:
                return i

    return -1

def CalcStrength(chain):
    result = 0
    for component in chain:
        for p in component.ports:
            result += p.value

    return result

def solve(input):
    lines = input.splitlines()

    components = []

    i = 0
    for line in lines:
        components.append(Component(line, i))
        i += 1

    chain = []
    highestStrength = 0
    i = 0
    maxLength = 0
    while True:
        port = 0
        if len(chain) != 0:
            port = chain[-1].GetFreePort()

        component = FindNextComponent(components, port, i)

        if component == -1:
            if len(chain) == 0:
                break

            strength = CalcStrength(chain)
            highestStrength = max(strength, highestStrength)
            maxLength = max(len(chain), maxLength)

            i = chain[-1].index + 1
            chain[-1].Reset()
            chain = chain[:-1]

        else:
            chain.append(components[component])
            i = 0

    print(maxLength)
    print(highestStrength)


solve("""25/13
4/43
42/42
39/40
17/18
30/7
12/12
32/28
9/28
1/1
16/7
47/43
34/16
39/36
6/4
3/2
10/49
46/50
18/25
2/23
3/21
5/24
46/26
50/19
26/41
1/50
47/41
39/50
12/14
11/19
28/2
38/47
5/5
38/34
39/39
17/34
42/16
32/23
13/21
28/6
6/20
1/30
44/21
11/28
14/17
33/33
17/43
31/13
11/21
31/39
0/9
13/50
10/14
16/10
3/24
7/0
50/50""")