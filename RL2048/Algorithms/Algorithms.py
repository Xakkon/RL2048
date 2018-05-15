from Environment.Game import Game
import random as rnd

def RandomTactic(game:Game):
    if(isinstance(game, Game)):
        moves = {0 : game.Up, 1 : game.Left, 2 : game.Down, 3 : game.Right}
        while(not game.EndGame):
            moves[rnd.randint(0,3)]()
        return game.Score, game.CountMoves

def CircleTactic(game:Game):
    if(isinstance(game, Game)):
        moves = {0 : game.Up, 1 : game.Right, 2 : game.Down, 3 : game.Left}
        i = rnd.randint(0,3)
        while(not game.EndGame):
            moves[i%4]()
            i += 1
        return game.Score, game.CountMoves

def AngleBagTactic(game:Game):
    if(isinstance(game, Game)):
        moves = {0 : game.Up, 1 : game.Right, 2 : game.Down, 3 : game.Left}
        i = 0
        prevScore = 0
        while(not game.EndGame):
            moves[i%2]()
            if((game.Score - prevScore) == 0):#
                moves[(i+1)%2]()
                if((game.Score - prevScore)==0):
                    moves[2]()
                    if((game.Score - prevScore)==0):
                        moves[3]()
            i += 1
            prevScore = game.Score
        return game.Score, game.CountMoves

def AngleTactic(game:Game):
    if(isinstance(game, Game)):
        moves = {0 : game.Up, 1 : game.Right, 2 : game.Down, 3 : game.Left}
        i = 0
        prevMoves = 0
        while(not game.EndGame):
            moves[i%2]()
            if((game.CountMoves - prevMoves) == 0):
                moves[(i+1)%2]()
                if((game.CountMoves - prevMoves)==0):
                    moves[2]()
                    if((game.CountMoves - prevMoves)==0):
                        moves[3]()
            i += 1
            prevMoves = game.CountMoves
        return game.Score, game.CountMoves

def AxisTactic(game:Game):
    if(isinstance(game, Game)):
        moves = [{0 : game.Up, 1 : game.Down}, {0 : game.Right, 1 : game.Left}]
        i = 0
        axis = 0
        prevMoves = 0
        emptyMoves = 0
        while(not game.EndGame):
            moves[axis%2][i%2]()
            if(game.CountMoves == prevMoves):
                axis += 1
                emptyMoves += 1
            else:
                emptyMoves = 0
            if(emptyMoves > 2):
                i += 1
            i += 1
            prevMoves = game.CountMoves
        return game.Score, game.CountMoves