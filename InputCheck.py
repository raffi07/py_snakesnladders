class InputCheck:
    def __init__(self):
        pass

    @staticmethod
    def board_size_input(sideType):
        size = input("Please provide {} of board: ".format(sideType))
        while not size.isdigit() or int(size) < 3 or int(size) > 100:
            size = input("Please enter a number between 3 and 100: ")
        return size

    @staticmethod
    def nameCheck(number):
        name = input("Player {} enter your name: ".format(str(number)))
        i = 0
        while i < len(name) or 0 >= len(name):
            if 0 >= len(name) or not name[i].isdigit() and not name[i].isalpha():
                name = input("Please use only letters and numbers in your name. Retry: ")
                i = 0
            else:
                i += 1
        return name
