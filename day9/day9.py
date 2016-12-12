def decompress(string):
    if not "(" in string:
        return len(string)
    length = 0
    while "(" in string:
        start = string.find("(")
        length += start
        end = string.find(")")
        marker = string[start+1:end]
        width, times = map(int, marker.split("x"))
        string = string[end+1:]
        length += decompress(string[:width]) * times
        string = string[width:]

    length += len(string)
    return length


def main():
    inputFile = open("input", "r")
    text = ""
    for line in inputFile.readlines():
        line = line.strip()
        text += line

    print decompress(text)


if __name__ == "__main__":
    main()
