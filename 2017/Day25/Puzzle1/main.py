class Action:
    def __init__(self, value, direction, state):
        self.value = value
        self.direction = direction
        self.state = state

class State:
    def __init__(self, actions):
        self.actions = actions

def solve(input):
    states = {
        'A': State([
            Action(1, 1, 'B'),
            Action(0, -1, 'B')
        ]),
        'B': State([
            Action(1, -1, 'C'),
            Action(0, 1, 'E')
        ]),
        'C': State([
            Action(1, 1, 'E'),
            Action(0, -1, 'D')
        ]),
        'D': State([
            Action(1, -1, 'A'),
            Action(1, -1, 'A')
        ]),
        'E': State([
            Action(0, 1, 'A'),
            Action(0, 1, 'F')
        ]),
        'F': State([
            Action(1, 1, 'E'),
            Action(1, 1, 'A')
        ])
    }

    state = 'A'
    tape = [ 0 ]
    cursor = 0

    for i in range(input):
        action = states[state].actions[tape[cursor]]

        tape[cursor] = action.value
        cursor += action.direction
        state = action.state

        if cursor == len(tape):
            tape.append(0)
        elif cursor == -1:
            tape = [ 0 ] + tape
            cursor += 1

    result = 0
    for value in tape:
        result += value

    print(result)

solve(12683008)