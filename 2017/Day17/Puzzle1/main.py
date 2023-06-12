import timeit

def solve(input):
    buffer = [0]
    position = 0

    cit = timeit.default_timer()

    for i in range(2017):
        position = (position + input) % len(buffer)
        buffer.insert(position + 1, i + 1)
        position += 1

    print(timeit.default_timer() - cit);

    print(buffer[(position + 1) % len(buffer)])

solve(304)