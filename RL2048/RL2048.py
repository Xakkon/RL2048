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
    gm = Game()

    plt.plot(Play(gm, alg.RandomTactic, iteration), 'r-',Play(gm, alg.CircleTactic, iteration),'b-',
            Play(gm, alg.AngleTactic, iteration), 'g-', Play(gm, alg.AngleBagTactic, iteration), 'y-.',
           Play(gm, alg.AxisTactic, iteration), 'k-')

    plt.show()

def Play(game:Game, tactic, iteration):
    lsTactic = []
    for i in range(iteration):
        game.NewGame()
        t = tactic(game)
        lsTactic.append(t)
    lsTactic.sort()
    return lsTactic

def main():
    #PlayOnConsole()
    PlayTactics(100)

if __name__ == "__main__":
    main()
