testCase = ['?1....1??',
            '?2....12?',
            '?1.....11',
            '11.......',
            '12221..11',
            '????2112?',
            '????21???',
            '????32???',
            '????2????']
h = 9
w = 9
nb = 12

bombProbs = []
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

    if bombsAround <= value:
        for uk in ukNeighbors:
            bombsFound.append(uk)
        row = list(testCase[cell[0]])
        row[cell[1]] = "0"
        testCase[cell[0]] = "".join(row)
        for n in get_neighbour(cell):
            if testCase[n[0]][n[1]] == "?":
                row = list(testCase[n[0]])
                row[n[1]] = "."
                testCase[n[0]] = "".join(row)
    return

# Main Function
for x in range(3):
    for row in testCase:
        print(row)
    print(" ")
    for x in range(h):
        for y in range(w):
            cur = (x, y)
            try:
                val = int(testCase[x][y])
                if val > 0:
                    search(cur, val)
            except ValueError:
                pass

print("x y")
for bomb in bombsFound:
    print("{} {}".format(bomb[0], bomb[1]))

# for row in testCase:
#     print(row)
