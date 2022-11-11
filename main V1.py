testCase = ['.1???1',
            '.11211',
            '11....',
            '?2....',
            '?1....',
            '11....']
h = 6
w = 6
m = 4

bombsFound = []


def get_neighbour(cell):
    neighbours = []
    x, y = cell

    cases = [-1, 0, 1]

    for x_cases in cases:
        for y_cases in cases:
            x_new = x + x_cases
            y_new = y + y_cases
            if (0 <= x_new < w) and (0 <= y_new < h):
                new_cell = (x_new, y_new)
                if cell != new_cell:
                    neighbours.append(new_cell)
    return neighbours


def search(cell, value):
    ukNeighbors = []
    bombsAround = 0
    for n in get_neighbour(cell):
        if n in bombsFound:
            value -= 1
        elif testCase[n[0]][n[1]] == "?":
            ukNeighbors.append(n)
            bombsAround += 1

    if bombsAround == value:
        for uk in ukNeighbors:
            bombsFound.append(uk)
    return

# Main Function

for x in range(h):
    for y in range(w):
        cur = (x, y)
        try:
            val = int(testCase[x][y])
            search(cur, val)
        except ValueError:
            pass


for b in bombsFound:
    print("{} {}".format(b[1], b[0]))
