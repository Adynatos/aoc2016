import string

def isMovePossible(x, y):
    if 0 <= y <= 4:
        if 0 <= x <= 4:
            return keypad[y][x] != 'x'
    return False

keypad = [['x', 'x', '1', 'x', 'x'],
          ['x', '2', '3', '4', 'x'],
          ['5', '6', '7', '8', '9'],
          ['x', 'A', 'B', 'C', 'x'],
          ['x', 'x', 'D', 'x', 'x']]

def main():
    lines = []
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        lines.append(string.strip(line))

    x, y = 0, 2

    keycode = ""

    for line in lines:
        for direction in line:
            n_x, n_y = x, y
            if direction == "U":
                n_y -= 1
            if direction == "R":
                n_x += 1
            if direction == "L":
                n_x -= 1
            if direction == "D":
                n_y += 1

            if isMovePossible(n_x, n_y):
                x, y = n_x, n_y
        keycode += keypad[y][x]

    print keycode

if __name__ == "__main__":
    main()
