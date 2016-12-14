class Bot(object):
    def __init__(self):
        self.low_to_bot = None
        self.high_to_bot = None
        self.visited = False

        self.values = []

    def update(self, value):
        self.values.append(value)
        self.values = sorted(self.values)


def main():
    inputFile = open("input", "r")
    bots = {}
    for line in inputFile.readlines():
        line = line.strip().split()
        if line[0] == "value":
            bot_id = int(line[-1])
            value = int(line[1])
            if not bot_id in bots:
                bots[bot_id] = Bot()
            bots[bot_id].values.append(value)
            bots[bot_id].values = sorted(bots[bot_id].values)

    inputFile.seek(0)

    for line in inputFile.readlines():
        line = line.strip().split()
        if line[0] == "bot":
            from_bot = int(line[1])
            low_to_bot = int(line[6])
            high_to_bot = int(line[-1])

            if from_bot not in bots:
                bots[from_bot] = Bot()

            if line[5] == "output":
                bots[from_bot].low_to = (low_to_bot, "output")
            else:
                bots[from_bot].low_to = (low_to_bot, "bot")

            if line[-2] == "output":
                bots[from_bot].high_to = (high_to_bot, "output")
            else:
                bots[from_bot].high_to = (high_to_bot, "bot")


    outputs = 21
    while(outputs):
        for bot_id in bots:
            bot = bots[bot_id]
            if len(bot.values) == 2:
                if bot.low_to[1] == "bot":
                    bots[bot.low_to[0]].update(bot.values[0])
                else:
                    print "Output %s has value %s" % (bot.low_to[0], bot.values[0])
                    outputs -= 1
                if bot.high_to[1] == "bot":
                    bots[bot.high_to[0]].update(bot.values[1])
                else:
                    print "Output %s has value %s" % (bot.high_to[0], bot.values[1])
                    outputs -= 1
                bots[bot_id].values = []



if __name__ == "__main__":
    main()
