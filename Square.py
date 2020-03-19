class Square:
    def __init__(self, number):
        self._number = number
        self.players = []

    def getPlayer(self):
        return self.players

    def enter(self, player):
        if not self.players:
            self.players.append(player)
            return True
        else:
            return False

    def printSquare(self):
        print("{}".format(self._number + 1), end="")
        for player in self.players:
            print("<{}>".format(player.getPlayerName()), end="")
