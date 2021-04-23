import tkinter as tk
import random
import ai
roundlist=[0] * 20
com = ai.Bot()
beat = {"R": "S", "P": "R", "S": "P"}
plist = [""] * 20
blist = [""] * 20
pscores = [0] * 20
bscores = [0] * 20

def game(p1, p2):  # output winner
    global result, plist, blist, pscores, bscores
    plist+=p1
    plist=plist[-20:]
    blist+=p2
    blist=blist[-20:]
    com.mainf(p1)
    if beat[p1] == p2:
        pscores.append(pscores[-1]+1)
        bscores.append(bscores[-1])
    elif beat[p2] == p1:
        bscores.append(bscores[-1]+1)
        pscores.append(pscores[-1])
    else:
        bscores.append(bscores[-1])
        pscores.append(pscores[-1])

    pscores = pscores[-20:]
    bscores = bscores[-20:]
    update()


r = tk.Tk()
r.title("Rock Paper Scissors")
gamescreen = tk.Frame(r, background="black")
gamescreen.pack_propagate(False)
gamescreen.pack()

top = tk.Frame(gamescreen)
top.grid(row=0, column=0, columnspan=4)
tt = tk.Label(top, text='Rock Paper Scissors!')
tt.pack()

rk=tk.PhotoImage(file="rock.png")
p=tk.PhotoImage(file="paper.png")
s=tk.PhotoImage(file="scissors.png")
left = tk.Frame(gamescreen)
left.grid(row=1, column=0)
rock = tk.Button(left, text="Rock", image=rk, command=lambda: game("R", com.output))
paper = tk.Button(left, text="Paper", image=p, command=lambda: game("P", com.output))
scissors = tk.Button(left, text="Scissors", image=s, command=lambda: game("S", com.output))
rock.grid(row=0, column=1)
scissors.grid(row=2, column=1)
paper.grid(row=1, column=1)

history = tk.Frame(gamescreen)
history.grid(row=1, column=2)
pdistitle = tk.Label(history, text="Player")
bdistitle = tk.Label(history, text="Bot")
pdistitle.grid(columnspan=2, row=0, column=1)
bdistitle.grid(columnspan=2, row=0, column=3)
def update():
    global r
    for i in range(20):
        pdisplay = tk.Label(history, text=plist[i])
        pdisplay.grid(row=20 - i, column=2)
        pscoredis = tk.Label(history, text=pscores[i])
        pscoredis.grid(row=20 - i, column=1)
        bdisplay = tk.Label(history, text=blist[i])
        bdisplay.grid(row=20 - i, column=4)
        bscoredis = tk.Label(history, text=bscores[i])
        bscoredis.grid(row=20 - i, column=3)
        rounds=tk.Label(history, text=roundlist[i-20])
        rounds.grid(row=20 - i, column=0)
    roundlist.append(roundlist[-1] + 1)
update()

r.mainloop()
