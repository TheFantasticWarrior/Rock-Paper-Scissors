import random
check = {"R": "S", "S": "P", "P": "R"}
encode = {"RR": "0", "SS": "1", "PP": "2",
          "RS": "3", "SP": "4", "PR": "5",
          "RP": "6", "SR": "7", "PS": "8"}
reverse = {"8": "4", "7": "3", "6": "5", "5": "6", "4": "8", "3": "7", "0": "0", "1": "1", "2": "2"}
encode2 = {"0": "1", "1": "1", "2": "1", "3": "2", "4": "2", "5": "2", "6": "3", "7": "3", "8": "3"}  # result


class Bot:
    def __init__(self):
        self.genes=[0, 90, 30, 7, 2, 0.8, 0.05, 5, 41, 63, 82, 710, 1000,
         37.5, 2.22, 0.62, 1.5, 0.82, -0.47, 0.23, 2]
        self.freq = [0] * 9
        self.ais = ["", "", "", "", "", "", "", ""]
        self.aips = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.last = ""
        self.output = random.choice("RPS")
    
    def default(self):
        for i in range(1,21):
            self.genes[i]=round(random.random()-0.5+self.genes[i]*(random.random()*3-0.5),2) 
        for i in range(7,12):
            self.genes[i]=int(self.genes[i])

    def __eq__(self,other):
        return self.score==other.score
    def calc(self, h, a, b):
        x = 0
        a = str(a)
        b = str(b)
        for i in range(5):
            x += h.count(b + a, len(h) - self.genes[i+7], len(h)) * self.genes[i+1]
        return x

    def algo(self, h):
        for i in range(9):
            self.freq[i] = self.calc(h, self.last, i) * self.genes[13]
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
        compare = {self.genes[14] * rchance - schance: "P", self.genes[14] * schance - pchance: "R",
                   self.genes[14] * pchance - rchance: "S"}
        return compare.get(max(compare))

    def accu_check(self, ai, aip):
        if ai != "":
            aip *= self.genes[15]
            if check[ai] == input:
                aip += self.genes[16]
            elif ai != input:
                aip -= self.genes[17]
            else:
                aip += self.genes[18]
        return aip

    def mainf(self, input):
        self.last = encode[input + self.output]
        for i in range(7):
            self.aips[i] = self.accu_check(self.ais[i], self.aips[i])
        self.aips[7] = self.aips[6] + 1

        self.ais[0] = self.algo(past)
        self.ais[1] = check[self.ais[0]]
        self.ais[2] = check[self.ais[1]]

        self.ais[3] = self.algo(cpast)
        self.ais[4] = check[self.ais[3]]
        self.ais[5] = check[self.ais[4]]
        self.ais[7] = self.ais[6] = random.choice("RPS")

        compare = self.aips[:]
        compare[self.aips.index(max(self.aips))] = -5000
        a = self.ais[self.aips.index(max(self.aips))]
        b = self.ais[compare.index(max(compare))]
        if max(self.aips) - max(compare) > self.genes[19]:
            self.output = a
        else:
            self.output = random.choices(population=a+b,weights=[self.genes[20],1])[0]
            
if input=="":
    past=""
    cpast = ""
    bot=Bot()
    bot.genes=genes#[58, 179.96, 10.63, -0.84, -0.68, 0.59, 0.31, 5, 17, 27, -30, -269, 2298.41, 81.84, 0.27, 1.57, 0.92, 1.71, -0.25, 0.31, 4.39]
    #print(bot.genes)
else:
    past += encode[input + output]
    cpast += reverse[encode[input + output]]
    bot.mainf(input)
output=bot.output