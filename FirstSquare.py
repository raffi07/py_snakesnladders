from Square import *


class FirstSquare(Square):
    def enter(self, player):
        self.players.append(player)
        return True
