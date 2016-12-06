def isPossible(sides):
    if sides[0] >= sides[1] + sides[2]:
        return False
    if sides[1] >= sides[0] + sides[2]:
        return False
    if sides[2] >= sides[1] + sides[0]:
        return False
    return True

def main():
    possible = 0
    lines = []
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        sides = line.split()
        sides = map(int, sides)
        lines += sides

    potential = lines[::3]
    potential += lines[1::3]
    potential += lines[2::3]


    for i in range(0, len(potential), 3):
        if isPossible((potential[i], potential[i+1], potential[i+2])):
            possible += 1

    print possible

if __name__ == "__main__":
    main()
