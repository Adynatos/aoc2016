import md5


def main():
    puzzle_input = "uqwqemis"
    password = {}
    index = 0
    while len(password) != 8:
        m = md5.new(puzzle_input + str(index)).hexdigest()
        while m[:5] != "00000":
            index += 1
            m = md5.new(puzzle_input + str(index)).hexdigest()
        print index, m
        if m[5].isdigit() and 0 <= int(m[5]) <= 8 and not m[5] in password:
            password[m[5]] = m[6]
            print password
        index += 1

    password = sorted(password.items(), key=lambda x: x[0])
    password = "".join((x[1] for x in password))
    print password


if __name__ == "__main__":
    main()
