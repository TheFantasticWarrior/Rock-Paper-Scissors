import random

rpsl = ['rock', 'scissors', 'paper']


class player:
    def __init__( self, choice=None, name=None ):
        self.choice = choice
        self.name = name
        self.score = 0

    def win( self ):
        self.score += 1
        if __name__ == '__main__':
            print('{} win'.format(self.name))


def RandomGame( choice, name ):
    p1.choice = choice
    p1.name=name
    if p1.choice == None:
        quit_()

    else:
        cpu.name="Computer"
        cpu.choice = random.choice(rpsl)
        output_choice(p1, cpu)
        if rpsl[(rpsl.index(cpu.choice) + 1) % 3] == p1.choice:
            cpu.win()
        elif rpsl[(rpsl.index(p1.choice) + 1) % 3] == cpu.choice:
            p1.win()
        else:
            even()
        output_score(p1, cpu)


def pvp( name1, name2 ):
    p1 = player(None, name1)
    p2 = player(None, name2)
    while True:
        get_input(p1)
        if p1.choice == None:
            quit_()
            break
        get_input(p2)
        if p2.choice == None:
            quit_()
            break
        output_choice(p1, p2)
        if rpsl[(rpsl.index(p1.choice) + 1) % 3] == p2.choice:
            p2.win()
        elif rpsl[(rpsl.index(p2.choice) + 1) % 3] == p1.choice:
            p1.win()
        else:
            even()
        output_score(p1, p2)


if __name__ == '__main__':
    from os import system, name

    rps = {'rock': 'rock',
           'r': 'rock',
           '0': 'rock',

           'paper': 'paper',
           'p': 'paper',
           '5': 'paper',

           'scissors': 'scissors',
           'scissor': 'scissors',
           's': 'scissors',
           '2': 'scissors'}


    def clear():
        if name == "nt":
            system("cls")
        else:
            system("clear")


    def even():
        print('The game is even')


    def output_choice( p1, p2 ):
        print('{} chose {}, {} chose {}'.format(p1.name, p1.choice, p2.name, p2.choice))


    def output_score( p1, p2 ):
        print('Score:\n{:^15} {:^15}\n{:^15} {:^15}'.format(p1.name, p2.name, p1.score, p2.score))


    def get_input( x ):
        a = input("{}'s turn, Please Choose Rock, Paper, Or Scissors: ".format(x.name)).lower()
        x.choice = rps.get(a)
        clear()


    def quit_():
        print("Invalid Key, Game Over")


    clear()
    gamemode = input("Play against computer or other player?\n".lower())

    if gamemode in ["computer", "c", "com", "cpu"]:
        name = input("Enter name: ").title()
        p1 = player(None, name)
        cpu = player(None, 'Computer')
        while True:
            choice = rps.get(input("{}'s turn, Please Choose Rock, Paper, Or Scissors: ".format(name)))
            RandomGame(choice, name)
    else:
        pvp(input("Enter Player 1 name: ").title(), input("Enter Player 2 name: ").title())
