# TODO read input from file

class CommandReader:

    _input = ""

    def __init__(self, ):
        self._input = open("BankTransIn.txt", "r")

    def print(self):
        print(self._input)


