import numpy as np
import random as rnd

class Game(object):
    def __init__(self, boardSize = 4):
        self.BoardSize = boardSize
        self.NewGame()

    def NewGame(self):
        self.Field = np.zeros((self.BoardSize, self.BoardSize))
        self._countSpaces = self.BoardSize**2
        self._score = 0
        self._AddRandomNumber()
        self._AddRandomNumber()

    def _AddRandomNumber(self):
        place = rnd.randint(0,self._countSpaces - 1)
        curPlace = 0
        wasPlaced = False
        for i in range(self.BoardSize):
            for j in range(self.BoardSize):
                if(self.Field[i,j] == 0):
                    if(curPlace == place):
                        self.Field[i,j] = 2 if (rnd.randint(0,100) <= 90) else 4
                        self._countSpaces -= 1
                        wasPlaced = True
                        break
                    else:
                        curPlace += 1
            if(wasPlaced):
                break

    def Up(self):
        prevScore = self._score
        self.Field = self.Field.transpose()
        self.Left()
        self.Field = self.Field.transpose()
        return self._Reward(prevScore)

    def Down(self):
        prevScore = self._score
        self.Field = np.flipud(self.Field)
        self.Up()
        self.Field = np.flipud(self.Field)
        return self._Reward(prevScore)

    def Right(self):
        prevScore = self._score
        self.Field = np.fliplr(self.Field)
        self.Left()
        self.Field = np.fliplr(self.Field)
        return self._Reward(prevScore)

    def Left(self):
        prevScore = self._score
        bias = False #было ли смещение
        for i in range(self.BoardSize):
            emptyPos = 0 #индекс места куда должна быть смещена плитка
            for j in range(self.BoardSize):
                if(self.Field[i,j] != 0):
                    #объединение двух плиток
                    for k in range(j+1, self.BoardSize):
                        if(self.Field[i,k] == self.Field[i, j]):
                            self.Field[i, j] = 2*self.Field[i,j]
                            self._score += self.Field[i, j]
                            self.Field[i, k] = 0
                            self._countSpaces += 1
                            bias = True
                            break
                        #если с первым ненулевым элементом справа нельзя объединить
                        elif(self.Field[i,k] != 0): 
                            break
                    #смещение плитки в левый край
                    if(j != emptyPos):
                        self.Field[i, emptyPos] = self.Field[i, j]
                        self.Field[i,j] = 0
                        bias = True
                    emptyPos += 1
        if(bias):
           self._AddRandomNumber()
        return self._Reward(prevScore)

    def _Reward(self, prevScore):
        return self._score - prevScore