# TODO read input from file

class CommandReader:

    import queue

    _file = open("BankTransIn.txt", "r")
    _lines_list = [""]

    def __init__(self):
        self._file = open("BankTransIn.txt", "r")
        self._lines_list = self._file.readlines()
        self.clean()

    # remove newline characters
    def clean(self):
        for x in range(len(self._lines_list)):
            self._lines_list[x] = self._lines_list[x].strip("\n")

    def print(self):
        print(self._lines_list)


