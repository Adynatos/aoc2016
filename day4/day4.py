from collections import Counter
from string import ascii_lowercase as alph


def alphCmp(a, b):
    if b[1] - a[1] == 0:
        return ord(a[0]) - ord(b[0])
    else:
        return b[1] - a[1]

def main():
    lines = []
    id_sum = 0
    inputFile = open("input", "r")
    for line in inputFile.readlines():
        line = line.strip()

        checksum_index = line.find("[")
        checksum = line[checksum_index:].strip("[]")
        rest = line[:checksum_index]

        id_index = rest.rfind("-")
        sector_id = line[id_index:checksum_index].replace("-", "")
        encrypted = line[:id_index].replace("-", "")

        counted = Counter(encrypted).most_common()
        s = sorted(counted, cmp=alphCmp)

        if checksum == "".join((x[0] for x in s[:5])):
            rotation = int(sector_id) % 26
            shifted = "".join((alph[(alph.find(i) + rotation) % 26] for i in encrypted if i != "-"))
            if shifted[0] == "n":
                print sector_id


if __name__ == "__main__":
    main()
