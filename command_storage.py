class CommandStorage:

    import queue

    _file = open("BankTransIn.txt", "r")
    _lines_list = [""]
    _q = queue.SimpleQueue()
    _size = 0

    # this class assumes there is already a BankTransIn.txt within the local directory
    def __init__(self):
        # open file
        self._file = open("BankTransIn.txt", "r")
        # read lines
        self._lines_list = self._file.readlines()
        # remove newline characters
        self.clean()
        # put into the queue
        for i in range(len(self._lines_list)):
            self._q.put(self._lines_list[i])
        # set number of commands in the queue
        self._size = self._q.qsize()

    # remove newline characters
    def clean(self):
        for i in range(len(self._lines_list)):
            self._lines_list[i] = self._lines_list[i].strip("\n")

    def get_size(self):
        return self._size

    def next_command(self):
        if self._q.empty():
            return "No commands left"
        else:
            return self._q.get()

    def print(self):
        for i in range(self._q.qsize()):
            print(self._q.get())

