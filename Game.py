from Board import *
from InputCheck import *
from Player import *
from Die import *


class Game:
    def __init__(self):
        self.board = None
        self.players = []
        self.dice = Die

    def gameLoop(self):
        input_check = InputCheck
        width = input_check.board_size_input("width")
        length = input_check.board_size_input("length")
        size = int(width) * int(length)
        playerOne = Player(input_check.nameCheck(1))
        playerTwo = Player(input_check.nameCheck(2))
        self.players.append(playerOne)
        self.players.append(playerTwo)
        self.board = Board(size, self.players)
        number = self.dice.throw()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()

