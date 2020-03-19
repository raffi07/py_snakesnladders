from Square import *


class Ladder(Square):
    def __init__(self, number, sendToNumber):
        super().__init__(number)
        self.sendToNumber = sendToNumber

    def enter(self, player):
        return self.sendToNumber

    def printSquare(self):
        print("{} -> {}".format(self._number,  self.sendToNumber), end="")
