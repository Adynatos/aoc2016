from collections import Counter


def main():
    lines = ""
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        line = line.strip()
        lines += line
    line_length = len(line)

    message = ""
    for i in range(line_length):
        chars = lines[i::line_length]
        c = Counter(chars).most_common()[-1][0]
        message += c
    print message

if __name__ == "__main__":
    main()
