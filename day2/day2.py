import string

def isMoveImpossible(position):
    return not  -2 < position < 2

def coordsToCode(coords):
    return str(5 - (3*coords[1]) + coords[0])

def main():
    lines = []
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        lines.append(string.strip(line))

    x, y = 0, 0

    keycode = []

    for line in lines:
        for direction in line:
            n_x, n_y = x, y
            if direction == "U":
                n_y += 1
            if direction == "R":
                n_x += 1
            if direction == "L":
                n_x -= 1
            if direction == "D":
                n_y -= 1

            if isMoveImpossible(n_x) or isMoveImpossible(n_y):
                continue
            x, y = n_x, n_y
        keycode.append((x, y))

    number = ""
    for coords in keycode:
        number += coordsToCode(coords)
    print number



if __name__ == "__main__":
    main()
