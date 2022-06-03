class CommandStorage:

    import queue

    _file = open("BankTransIn.txt", "r")
    # commands are stored in a queue
    _q = queue.SimpleQueue()
    _size = 0

    # this class assumes there is already a BankTransIn.txt within the local directory
    def __init__(self):
        # open file
        self._file = open("BankTransIn.txt", "r")
        # read lines
        lines = self._file.readlines()
        # remove newline characters
        for i in range(len(lines)):
            lines[i] = lines[i].strip("\n")
        # put into the queue
        for i in range(len(lines)):
            self._q.put(lines[i])
        # set number of commands in the queue
        self._size = self._q.qsize()

    def get_size(self):
        return self._size

    def get_command(self):
        if self._q.empty():
            return "Empty"
        else:
            return self._q.get()
