def main():
    impossible = 0
    every = 0
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        every += 1
        sides = line.split()
        sides = map(int, sides)
        if sides[0] >= sides[1] + sides[2]:
            impossible += 1
        if sides[1] >= sides[0] + sides[2]:
            impossible += 1
        if sides[2] >= sides[1] + sides[0]:
            impossible += 1

    print every - impossible
if __name__ == "__main__":
    main()
