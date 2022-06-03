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

    # Reads and stores the values'
    # error handling goes in here
    def parse(self, command: string = ""):
        # break the string into a list
        self._command = command.split()
        self._command_type = command[0]

        if self._command_type == "O":
            print("Open")
            self._last_name = self._command[1]
            self._first_name = self._command[2]
            if len(self._command[3]) > 4:
                print("Account numbers may only be four digits.\n Example: 1234")
            else:
                self._account_number = self._command[3]
        # opening an account is the only command that has letters
        else:
            account_number_long = self._command[1]
            if len(account_number_long) > 5:
                print("Account number is too long.")
            if len(account_number_long) == 5:
                self._account_number = account_number_long[0:4]
                self._account_type = account_number_long[4]
            else:
                self._account_number = account_number_long

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

    # # TODO performs the transaction
    # def transact(self, command: string = ""):
    #     self.parse(command)
    #
    #     if self._command_type == "O":
    #         # TODO create new account object
    #         # TODO add to the BST
    #
    #     if self._command_type == "D":
    #         # TODO locate account in BST
    #         # TODO increase amount by self._amount
    #
    #     if self._command_type == "W":
    #         # TODO locate account in BST
    #         if account.amount > self.amount:
    #             # TODO decrease amount by self._amount
    #         else:
    #             print("You do not have enough funds.")
    #
    #     if self._command_type == "T":
    #         # TODO locate account in BST
    #         # TODO locate account2 in BST
    #         if account.amount > self.amount:
    #             # TODO decrease amount by self._amount
    #             # TODO increase account2 by self._amount
    #         else:
    #             # handling shared money market fund overdraws
    #             if account.amount > self.amount:
    #                 # TODO decrease self._amount by amount
    #                 # TODO set amount to $0
    #                 # TODO decrease OTHER MM fund amount by self._amount
    #                 # TODO increase account2 by self._amount
    #             else:
    #                 print("You do not have enough funds.")
    #
    #     if self._command_type == "H":
    #         # TODO print history
    #         print(f"Transaction History for {self._first_name} {self._last_name} by fund.")

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
