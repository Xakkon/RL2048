from Environment.Game import Game

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

def main():
    PlayOnConsole()

if __name__ == "__main__":
    main()
