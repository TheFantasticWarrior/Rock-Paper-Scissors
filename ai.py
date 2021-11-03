import random
import numpy as np
genetic=False
debug=False
if debug:
    genetic=False
readpath="dllu.txt"
outpath="dllu2.txt"
check = {"R": "S", "S": "P", "P": "R"}
encode = {"RR": "0", "SS": "1", "PP": "2",
          "RS": "3", "SP": "4", "PR": "5",
          "RP": "6", "SR": "7", "PS": "8"}
reverse = {"8": "4", "7": "3", "6": "5", "5": "6", "4": "8", "3": "7", "0": "0", "1": "1", "2": "2"}
encode2 = {"0": "1", "1": "1", "2": "1", "3": "2", "4": "2", "5": "2", "6": "3", "7": "3", "8": "3"}  # result

def score_calc(x):
    if x in ["3","4","5"]:
        return -1
    elif x in ["6","7","8"]:
        return 1
    else:
        return 0


class Bot:
    def __init__(self,i):
        self.score=0
        self.genes=[i, 90, 30, 7, 2, 0.8, 0.05, 5, 41, 63, 82, 710, 1000,
         37.5, 2.22, 0.62, 1.5, 0.82, -0.47, 0.23, 2]
        
        self.freq = [0] * 9
        self.ais = ["","","","","","",""]
        self.aips = [-1, -1, -1, -1, -1, -1, 0.5]
        self.last = ""
        self.output = random.choice("RPS")
    
    def default(self):
        for i in range(1,21):
            self.genes[i]=round(random.random()-0.5+self.genes[i]*(random.random()*3-0.5),2) 
        for i in range(7,12):
            self.genes[i]=int(self.genes[i])
        self.point = self.genes[1:6]
        self.length = self.genes[7:12]
    
    def read(self):
        self.genes=genes[self.genes[0]]
        self.point = self.genes[1:6]
        self.length = self.genes[7:12]


    def __eq__(self,other):
        return self.score==other.score
    def calc(self, h, a, b):
        x = 0
        a = str(a)
        b = str(b)
        for i in range(len(self.length)):
            x += h.count(b + a, len(h) - self.length[i], len(h)) * self.point[i]
        return x

    def algo(self, h,r):
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
        if r:
            rchance = self.freq[0] + self.freq[7] + self.freq[5]
            schance = self.freq[1] + self.freq[3] + self.freq[8]
            pchance = self.freq[2] + self.freq[4] + self.freq[6]
        else:
            rchance = self.freq[0] + self.freq[3] + self.freq[6]
            schance = self.freq[1] + self.freq[4] + self.freq[7]
            pchance = self.freq[2] + self.freq[5] + self.freq[8]
        compare = {self.genes[14] * rchance - schance: "P", self.genes[14] * schance - pchance: "R",
                   self.genes[14] * pchance - rchance: "S"}
        #return {"P":pchance, "R":rchance,"S":schance}
        return compare.get(max(compare))

    def points_calc2(self):
        correct=[]
        def points_calc(self, ai, aip):
            nonlocal correct
            if ai != "":
                aip *= self.genes[15]
                aip=round(aip,2)
                if check[ai] == input:
                    aip += self.genes[16]
                    correct.append(x)
                elif ai != input:
                    aip -= self.genes[17]
                else:
                    aip += self.genes[18]
            return aip
        for x in range(6):
            self.aips[x] = points_calc(self,self.ais[x], self.aips[x])
        clist.append(correct[:])

    def mainf(self, input):
        self.last = encode[input + self.output]
        self.score+=score_calc(self.last)
        self.points_calc2()

        self.ais[0] = self.algo(past,False)
        self.ais[1] = check[self.ais[0]]
        self.ais[2] = check[self.ais[1]]

        self.ais[3] = self.algo(cpast,False)
        self.ais[4] = check[self.ais[3]]
        self.ais[5] = check[self.ais[4]]
        self.ais[6] = random.choice("RPS")
        compare = self.aips[:]
        for _ in range(2):
            compare[compare.index(max(compare))] = -5000
        best=self.aips.index(max(self.aips))
        a = self.ais[best]
        b = self.ais[compare.index(max(compare))]
        blist.append(best)
        if max(self.aips) - max(compare) >self.genes[19]:
            self.output = a
        else:
            self.output = random.choices(population=a+b+random.choice("RPS"),weights=[self.genes[20],1,1])[0]
            

def genesmodify(size,inp,out):
    f=open(inp,"r+")
    data=f.readlines()
    data.sort(reverse=True)
    """f.seek(0)
    for x in data[:50]:
        f.write(x)
    f.truncate()"""
    f.close()
    pop=len(data)
    genes=[[i if x==0 else elem for x,elem in enumerate(eval(data[i])[1])] for i in range(pop)]
    weights=[round((5+eval(data[i])[0])**0.5,1) for i in range(pop)]
    def swap(n,x,y):
        conv=random.randint(1,len(x))
        a=x[:conv]+y[conv:]
        a[0]=n
        b=y[:conv]+x[conv:]
        b[0]=n+1
        return [a,b]

    for i in range(round((size-pop)/2)):
        x,y=random.choices(range(pop),weights=weights,k=2)
        genes+=swap(i*2+pop,genes[x],genes[y])

    rng = np.random.default_rng()
    mutate=rng.integers([0,1],[len(genes),21],(5,2))
    for i in mutate:
        genes[i[0]][i[1]]=round((genes[i[0]][i[1]]+(random.random()-0.5))*(random.random()*2-1),2)
        if i[1] in range(7,13):
            genes[i[0]][i[1]]=int(round(genes[i[0]][i[1]]))

    n=open(out,"w")
    for x in genes:
        n.write(f"{x}\n")
    n.close()


if __name__=="builtins" or __name__=="__builtin__":
    if input=="":
        bots=[]
        past=""
        cpast = ""
        rounds=0
        points=[]
        clist=[]
        blist=[]
        try:
            f=open(readpath,"r")
            genes=[eval(i) for i in f.readlines()]
            if debug:
                genes=genes[0]
            f.close()
            pop=len(genes)
            for i in range(pop):
                bots.append(Bot(i))
                bots[i].read()
        except: 
            if not debug:
                pop=100
            for i in range(pop):
                bots.append(Bot(i))
                bots[i].default()
    else:
        past += encode[input + output]
        cpast += reverse[encode[input + output]]
        for bot in bots:
            bot.mainf(input)
        
    bots.sort(key=lambda x:x.score,reverse=True)
    output=bots[0].output
    rounds+=1
    points.append(bots[0].aips[:])
    """if rounds%10==0:
        results=[score_calc(i) for i in past[-100:]]
        f=open("p.txt","a")
        f.write(f"{[bots[0].score,sum(results)]}\n")
        f.close()"""
    if rounds==1000 and genetic:
        f=open(outpath,"w")
        f.writelines([str([bot.score,bot.genes])+"\n" for bot in bots if bot.score>-5])
        f.close()
        f=open("points.txt","w")
        f.writelines([str(point)+"\n" for point in points])
        f.close()
        genesmodify(100,outpath,readpath)
    if rounds==500:
        f=open("mid.txt","w")
        f.writelines([str([bot.score,bot.genes])+"\n" for bot in bots if bot.score>-5])
        f.close()
    if rounds==1000 and debug:
        print(bots[0].genes)
        for i in range(998):
            print(blist[i],clist[i+1])
        print(past)
        print(cpast)
