from Square import *
from FirstSquare import *
from Snake import *
from Ladder import *
from random import randint


class Board:
    def __init__(self, size, players):
        self._size = size
        self.players = players
        self.board = self.initEmptyBoard()
        self.setSpecialFields()
        self.printBoard()

    def initEmptyBoard(self):
        board = [FirstSquare(0)]
        for player in self.players:
            board[0].enter(player)
        for i in range(1, self._size):
            board.append(Square(i))
        return board

    def printBoard(self):
        for i in range(0, self._size):
            print("[", end="")
            self.board[i].printSquare()
            print("]", end="")

    @staticmethod
    def getRandomNumber(lowerBound, upperBound):
        return randint(lowerBound, upperBound)

    def isSpecialField(self, number):
        return type(self.board[number]) is Snake or type(self.board[number]) is Ladder

    def setSpecialFields(self):
        specialFieldCap = self._size // 4
        snakeCap = specialFieldCap // 2
        ladderCap = specialFieldCap // 2
        maxLength = self._size // 3
        self.setSnakes(snakeCap, maxLength)
        self.setLadders(ladderCap, maxLength)

    def setSnakes(self, snakeCap, maxLength):
        count = 0
        while count <= snakeCap:
            maximumIterations = 0
            randomNumber = self.getRandomNumber(3, self._size - 2)
            while self.isSpecialField(randomNumber):
                randomNumber = self.getRandomNumber(3, self._size - 2)
            randomPartner = self.getRandomNumber(
                2 if (randomNumber - maxLength < 2) else (randomNumber - maxLength),
                randomNumber - 1)
            while self.isSpecialField(randomPartner) and (maximumIterations <= self._size*2):
                maximumIterations += 1
                randomPartner = self.getRandomNumber(
                    2 if (randomNumber - maxLength < 2) else (randomNumber - maxLength),
                    randomNumber - 1)
            if not self.isSpecialField(randomPartner):
                self.board[randomNumber] = Snake(randomNumber+1, randomPartner+1)
                count += 1

    def setLadders(self, ladderCap, maxLength):
        count = 0
        while count <= ladderCap:
            maximumIterations = 0
            randomNumber = self.getRandomNumber(1, self._size - 3)
            while self.isSpecialField(randomNumber):
                randomNumber = self.getRandomNumber(1, self._size - 3)
            randomPartner = self.getRandomNumber(randomNumber + 1,
                                                 self._size - 2 if (randomNumber + maxLength > self._size - 2)
                                                 else randomNumber + maxLength)
            while self.isSpecialField(randomPartner) and (maximumIterations <= self._size*2):
                maximumIterations += 1
                randomPartner = self.getRandomNumber(randomNumber + 1,
                                                     self._size - 2 if (randomNumber + maxLength > self._size - 2)
                                                     else randomNumber + maxLength)
            if not self.isSpecialField(randomPartner):
                self.board[randomNumber] = Ladder(randomNumber+1, randomPartner+1)
                count += 1
