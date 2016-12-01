import string
from enum import Enum


def main():
    directions = []
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        directions += map(string.strip, line.split(","))

    x, y = 0, 0
    visited = set((x, y))
    facing = (0, 1)
    for direction in directions:
        distance = int(direction[1:])
        if direction[0] == "R":
            facing = facing[1], -facing[0]
        elif direction[0] == "L":
            facing = -facing[1], facing[0]

        for step in range(distance):
            x += facing[0]
            y += facing[1]
            if (x, y) in visited:
                print "Result is: {0} = point is ({1}, {2})".format(abs(x) + abs(y), x, y)
                return
            visited.add((x,y))


if __name__ == "__main__":
    main()
