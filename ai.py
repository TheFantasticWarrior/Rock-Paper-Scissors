import random

check = {"R": "S", "S": "P", "P": "R"}
encode = {"RR": "0", "SS": "1", "PP": "2",
          "RS": "3", "SP": "4", "PR": "5",
          "RP": "6", "SR": "7", "PS": "8"}
reverse = {"8": "4", "7": "3", "6": "5", "5": "6", "4": "8", "3": "7", "0": "0", "1": "1", "2": "2"}
encode2 = {"0": "1", "1": "1", "2": "1", "3": "2", "4": "2", "5": "2", "6": "3", "7": "3", "8": "3"}  # result


class Bot:
    def __init__(self):
        self.point = [64, 24, 12, 2, 0.3]
        self.length = [10, 30, 50, 100, 500]
        self.freq = [0] * 9
        self.ais = ["", "", "", "", "", "", "", ""]
        self.aips = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.past = ""
        self.last = ""
        self.output = random.choice("RPS")

    def calc(self, h, a, b):
        x = 0
        a = str(a)
        b = str(b)
        for i in range(len(self.length)):
            x += h.count(b + a, len(h) - self.length[i], len(h)) * self.point[i]
        return x

    def algo(self, h):
        for i in range(9):
            self.freq[i] = self.calc(h, self.last, i) * 60
        if encode2[self.last] == 1:
            for i in range(9):
                for b in [0, 1, 2]:
                    self.freq[i] += self.calc(h, i, b)
        elif encode2[self.last] == 2:
            for i in range(9):
                for b in [3, 4, 5]:
                    self.freq[i] += self.calc(h, i, b)
        else:
            for i in range(9):
                for b in [6, 7, 8]:
                    self.freq[i] += self.calc(h, i, b)
        rchance = self.freq[0] + self.freq[3] + self.freq[6]
        schance = self.freq[1] + self.freq[4] + self.freq[7]
        pchance = self.freq[2] + self.freq[5] + self.freq[8]
        compare = {2 * rchance - schance: "P", 2 * schance - pchance: "R",
                   2 * pchance - rchance: "S"}
        return compare.get(max(compare))

    def accu_check(self, ai, aip):
        if ai != "":
            aip *= 0.6
            if check[ai] == input:
                aip += 1
            elif ai != input:
                aip -= 1
            else:
                aip += 0
        return aip

    def mainf(self, input):
        self.last = encode[input + self.output]
        self.past += self.last
        self.past = self.past[-500:]
        for i in range(7):
            self.aips[i] = self.accu_check(self.ais[i], self.aips[i])
        self.aips[7] = self.aips[6] + 1

        self.ais[0] = self.algo(self.past)
        self.ais[1] = check[self.ais[0]]
        self.ais[2] = check[self.ais[1]]
        cpast = ""
        for c in self.past:
            cpast += reverse[c]
        self.ais[3] = self.algo(cpast)
        self.ais[4] = check[self.ais[3]]
        self.ais[5] = check[self.ais[4]]
        self.ais[7] = self.ais[6] = random.choice("RPS")

        compare = self.aips[:]
        compare[self.aips.index(max(self.aips))] = -5000
        a = self.ais[self.aips.index(max(self.aips))]
        b = self.ais[compare.index(max(compare))]
        if max(self.aips) - max(compare) > 0.5:
            self.output = a
        else:
            self.output = random.choice(a + a + b)


if __name__ == '__main__':
    first = Bot()
    for i in range(1000):
        print(first.output)
        inp = input(":")
        if inp == "q":
            break
        else:
            first.mainf(inp)