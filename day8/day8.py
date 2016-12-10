def rotate(l, n):
    return l[-n:] + l[:-n]

def main():
    inputFile = open("input", "r")
    row = "."*50
    rect = [row] * 6
    for line in inputFile.readlines():
        line = line.strip()
        line = line.split()

        if line[0] == "rect":
            width, height = map(int, line[1].split("x"))
            for i in range(height):
                rect[i] = "#"*width + rect[i][width:]
        if line[0] == "rotate":
            target = int(line[2][2:])
            rotation = int(line[-1])
            print rotation
            if line[1] == "row":
                rect[target] = rotate(rect[target], rotation)
            if line[1] == "column":
                col = "".join((row[target] for row in rect))
                col = rotate(col, rotation)
                for row, px in enumerate(col):
                    rect[row] = rect[row][:target] + px + rect[row][target+1:]

        print "\n".join(rect)
        print "\n"

    count = 0
    for row in rect:
        count += row.count("#")

    print count


if __name__ == "__main__":
    main()
