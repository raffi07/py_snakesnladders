from random import randint


class Die:
    def __init__(self):
        pass

    @staticmethod
    def throw():
        return randint(1, 6)
