from Environment.Game import Game
from Algorithms import Algorithms as alg
import matplotlib.pyplot  as plt
import statistics as stat

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
    Play(gm, alg.RandomTactic, iteration, 'r-', 'Random')
    Play(gm, alg.CircleTactic, iteration, 'b-', 'Circle')
    Play(gm, alg.AngleTactic, iteration, 'g-', 'Angle')
    Play(gm, alg.AxisTactic, iteration, 'k-', 'Axis')

    plt.show()

    """lsPeople = [1380, 1232, 2440, 1128, 1032, 1496, 1316, 1992, 14352, 27124,
                2724, 27076, 440, 1424, 2892, 5500, 3100, 2500,  1664, 1240,
                2632, 2760, 892, 644, 1340, 100980, 1312, 2552, 5452, 1420,
                2700]
    lsPeople.sort()

    plt.plot(lsPeople, 'y-')
    print('People', ':')
    print('max = ', max(lsPeople))
    print('min = ', min(lsPeople))
    print('average = ', stat.mean(lsPeople))
    print('median = ', stat.median(lsPeople), '\n')
    plt.show()"""

def Play(game:Game, tactic, iteration:int, line:str, title:str):
    lsScore = []
    lsSteps = []
    for i in range(iteration):
        game.NewGame()
        score, step = tactic(game)
        lsScore.append(score)
        lsSteps.append(step)
    maxStep = lsSteps[lsScore.index(max(lsScore))]
    minStep = lsSteps[lsScore.index(min(lsScore))]
    lsScore.sort()
    plt.plot(lsScore, line)
    print(title, ':')
    print('max = ', max(lsScore), ' steps = ', maxStep)
    print('min = ', min(lsScore), ' steps = ', minStep)
    print('average = ', stat.mean(lsScore), ' steps = ', stat.mean(lsSteps))
    print('median = ', stat.median(lsScore), ' steps =', stat.median(lsSteps), '\n')
    return 0

def main():
    #PlayOnConsole()
    PlayTactics(10000)

if __name__ == "__main__":
    main()
