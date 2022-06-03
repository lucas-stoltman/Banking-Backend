# this class performs the commands it receives
class Transaction:
    import string

    _command = []
    _command_type = None
    _account_number = None
    _account_type = None
    _account2_number = None
    _account2_type = None
    _last_name = None
    _first_name = None
    _amount = 0

    # TODO error handling goes in here
    # Reads and stores the values
    def parse(self, command: string = ""):
        # break the string into a list
        self._command = command.split()
        self._command_type = command[0]

        if self._command_type == "O":
            print("Open")
            self._last_name = self._command[1]
            self._first_name = self._command[2]
            self._account_number = self._command[3]
        # opening an account is the only command that has letters
        else:
            account_number_long = self._command[1]
            self._account_number = account_number_long[:-1]
            self._account_type = account_number_long[-1:]

            if self._command_type == "D":
                print("Deposit")
                self._amount = self._command[2]

            if self._command_type == "W":
                print("Withdraw")
                self._amount = self._command[2]

            if self._command_type == "T":
                print("Transfer")
                self._amount = self._command[2]
                account2_number_long = self._command[3]
                self._account2_number = account2_number_long[:-1]
                self._account2_type = account2_number_long[-1:]

            if self._command_type == "H":
                print("History")
                self._account_number = self._command[1]

    # performs the transaction
    def transact(self, command: string = ""):
        self.parse(command)

    # only for debug purposes
    def print_debug(self):
        print("------------------------")
        print(self._command)
        print("Command Type:", self._command_type)
        if self._last_name:
            print("Last Name:", self._last_name)
        if self._first_name:
            print("First Name:", self._first_name)
        if self._account_number:
            print("Account Number:", self._account_number)
        if self._account_type:
            print("Account Type:", self._account_type)
        if self._amount:
            print("Amount:", f"${self._amount}")
        if self._account2_number:
            print("Account2 Number:", self._account2_number)
        if self._account2_type:
            print("Account2 Type:", self._account2_type)
