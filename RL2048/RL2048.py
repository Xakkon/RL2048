from Environment.Game import Game
from Algorithms import Algorithms as alg
import matplotlib.pyplot  as plt

def PlayOnConsole():
    gm = Game()
    c = ""
    moves = {'w' : gm.Up, 'a' : gm.Left, 's' : gm.Down, 'd' : gm.Right, 'n' : gm.NewGame}
    print("w = Up, a = Left, s = Down, d = Right, n = NewGame, 0 = Exit")
    print("Score =",gm._score)
    print(gm.Field)
    while c != "0":
        c = input()
        if (c in moves):
            moves[c]()
            print("Score =",gm._score)
            print(gm.Field)

def PlayTactics(iteration:int):
    lsRandom = []
    gm = Game()
    for i in range(iteration):
        gm.NewGame()
        t = alg.RandomTactic(gm)
        lsRandom.append(t)

    lsCircle = []
    for i in range(iteration):
        gm.NewGame()
        t = alg.CircleTactic(gm)
        lsCircle.append(t)

    lsAngle = []
    for i in range(iteration):
        gm.NewGame()
        t = alg.AngleTactic(gm)
        lsAngle.append(t)
    
    lsAngleBag = []
    for i in range(iteration):
        gm.NewGame()
        t = alg.AngleBagTactic(gm)
        lsAngleBag.append(t)

    lsCircle.sort()
    lsRandom.sort()
    lsAngle.sort()
    lsAngleBag.sort()
    plt.plot(lsRandom, 'r--',lsCircle, 'b--', lsAngle, 'g--', lsAngleBag, 'y--')
    plt.show()

def main():
    #PlayOnConsole()
    PlayTactics(5)

if __name__ == "__main__":
    main()
