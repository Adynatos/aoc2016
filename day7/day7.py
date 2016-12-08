def isAba(string):
    if len(string) < 3:
        return False
    return string[0] == string[-1] and string[0] != string[1]

def invert(string):
    return string[1] + string[0] + string[1]

def main():
    lines = ""
    count = 0
    bab = []
    aba = []
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        line = line.strip()
        bab = []
        aba = []
        found = False
        line = line.replace("]", "[")
        line = line.split("[")
        tags = line[1::2]

        for tag in tags:
            for i in range(len(tag)):
                substr = tag[i:i+3]
                if isAba(substr):
                    bab.append(invert(substr))

        if not bab:
            continue


        rests = line[::2]
        for rest in rests:
            for i in range(len(rest)):
                substr = rest[i:i+3]
                if isAba(substr):
                    aba.append(substr)

        for a in aba:
            if a in bab:
                count += 1
                break

    print count

if __name__ == "__main__":
    main()
