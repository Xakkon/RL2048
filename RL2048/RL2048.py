from Environment.Game import Game

def PlayOnConsole():
    gm = Game()
    c = ""
    print("w = Up, a = Left, s = Down, d = Right, n = NewGame, 0 = Exit")
    print("Score =",gm._score)
    print(gm.Field)
    while c != "0":
        c = input()
        if(c == "w"):
            gm.Up()
        elif(c == "a"):
            gm.Left()
        elif(c == "s"):
            gm.Down()
        elif(c == "d"):
            gm.Right()
        elif(c == "n"):
            gm.NewGame()
        print("Score =",gm._score)
        print(gm.Field)

PlayOnConsole()
