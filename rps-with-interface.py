import tkinter as tk
import random
rps=["rock","paper","scissor"]
class player():
    def __init__(self, choice=None, name=None):
        self.choice=choice
        self.name=name
        self.score=0
    def win( self ):
        self.score+=1


def game_setup(opponent):
    global name,name_box,nl,send,cpu,p1,p2
    del_(cpu,human,ai,op)
    p1=player()
    if opponent == "com":
        cpu = player(random.choice(rps), "Computer")
        nl=tk.Label(top, text="Enter Your Name")
        nl.pack()
        name_box=tk.Entry(mid)
        name_box.pack()
    else:
        p2 = player()
        p1ne=tk.Label(top,text="Player 1's name:")
        p1ne.grid(row=0)
        p1e=tk.Entry(top)
        p1e.grid(row=0,column=1)
        p2ne = tk.Label(top, text="Player 2's name:")
        p2ne.grid(row=1)
        p2e = tk.Entry(top)
        p2e.grid(row=1, column=1)
    send=tk.Button(mid,text="Confirm",command=callback)
    send.grid(columnspan=2)




def callback():
    global r,p,s,text
    name_=name_box.get()
    p1.name=name_
    del_(nl,name_box,send)
    text=tk.Label(top,text="Choose one")
    text.pack()
    #choice
    r=tk.Button(mid,text="Rock",command=lambda: chose(name_, "rock"))
    r.pack(side="left")
    p=tk.Button(mid,text="Paper",command=lambda: chose(name_, "paper"))
    p.pack(side="left")
    s=tk.Button(mid,text="Scissors",command=lambda: chose(name_, "scissors"))
    s.pack(side="left")


def output_choice(p1, p2):
    p1n=tk.Label(top,text=p1.name)
    p1n.grid()
    p2n = tk.Label(top, text=p2.name)
    p2n.grid(row=0,column=1)
    p1c = tk.Label(top, text=p1.choice)
    p1c.grid(row=1)
    p2c = tk.Label(top, text=p2.choice)
    p2c.grid(row=1, column=1)

def chose(name, choice):
    del_(r,p,s,text)
    #RandomGame(choice,name)

def del_(*args):
    for arg in args:
        arg.destroy()


window=tk.Tk()
window.title("Rock Paper Scissors")
#window.geometry("480x360")
#window.resizable(0,0)
top=tk.Frame(window).pack(side='top')
op=tk.Label(top,text="Choose Your Opponent")
op.pack()

mid=tk.Frame(window).pack(side='top')

cpu=tk.Button(mid, text="Computer", command=lambda: game_setup("com"))
cpu.pack()
human=tk.Button(mid, text="Another Human Player", command=lambda: game_setup("human"))
human.pack()
ai=tk.Button(mid, text="Coming Soon...", state="disabled")
ai.pack()

bottom=tk.Frame(window).pack(side="top")
button=tk.Button(bottom,text="quit",fg="red",command=window.destroy).pack(side="bottom")

window.mainloop()
