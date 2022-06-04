# this class performs the commands it receives
class Transaction:
    import string

    def __init__(self):
        self._command = []
        self._command_type = None
        self._account_number = None
        self._fund_type = None
        self._account2_number = None
        self._fund2_type = None
        self._last_name = None
        self._first_name = None
        self._amount = float(0)

    # Reads and stores the values'
    # error handling goes in here
    def parse(self, command: string):
        # break the string into a list
        self._command = command.split()
        self._command_type = command[0]

        if self._command_type == "O":
            self._last_name = self._command[1]
            self._first_name = self._command[2]
            if len(self._command[3]) > 4:
                print("Account numbers may only be four digits.\n Example: 1234")
            else:
                self._account_number = int(self._command[3])
        # opening an account is the only command that has letters
        else:
            account_number_long = self._command[1]
            if len(account_number_long) > 5:
                print("Account number is too long.")
            elif len(account_number_long) == 5:
                self._account_number = account_number_long[0:4]
                self._fund_type = account_number_long[4]
            else:
                self._account_number = account_number_long

            if self._command_type == "D":
                self._amount = float(self._command[2])
            elif self._command_type == "W":
                self._amount = float(self._command[2])
            elif self._command_type == "T":
                self._amount = float(self._command[2])
                account2_number_long = self._command[3]
                self._account2_number = account2_number_long[:-1]
                self._fund2_type = account2_number_long[-1:]
            elif self._command_type == "H":
                self._account_number = self._command[1]
            else:
                print("Unrecognized command.")

    # TODO performs the transaction
    def transact(self, command: string):
        import main
        from account import Account
        from fund import Fund
        from account_storage import Node, BST

        self.parse(command)

        if self._command_type == "O":
            # create new account object
            account = Account(self._account_number, self._last_name, self._first_name)
            node = Node(account.get_number(), account)
            # add to the BST
            main.storage.put(node.key, node)
            # print(f"\tOpened an account for {self._first_name} {self._last_name} ({self._account_number})")

        if self._command_type == "D":
            # locate account in BST
            account = main.storage.get(int(self._account_number)).value
            # if fund not found, open fund
            if not account.find_fund(self._fund_type):
                new_fund = Fund(account.get_number, self._fund_type, self._amount)
                # increase account.fund.amount by transaction._amount
                account.add_fund(new_fund)
                # print(f"\tAdded ${self._amount} to fund {self._fund_type}")
                return True
            else:
                # increase fund by self._amount
                fund = account.get_fund(self._fund_type)
                fund += self._amount
                # print(f"\tAdded ${self._amount}")
                return True

        if self._command_type == "W":
            #  locate account in BST
            account = main.storage.get(int(self._account_number)).value
            fund_balance = account.get_fund(int(self._fund_type)).get_balance()
            # print("\tBalance Before:\t", fund_balance)
            if fund_balance >= self._amount:
                # TODO decrease account.amount by transaction._amount
                account.get_fund(int(self._fund_type)).change_balance(-abs(self._amount))
                # print("\tBalance After:\t", account.get_fund(int(self._fund_type)).get_balance())
            else:
                print("You do not have enough funds.")

        if self._command_type == "T":
            # locate account1 in BST
            account1 = main.storage.get(int(self._account_number)).value
            # locate account2 in BST
            if main.storage.get(self._account2_number) is not None:
                account2 = main.storage.get(int(self._account2_number)).value
                # remove money from first fund
                account1.get_fund(int(self._fund_type)).change_balance(-abs(self._amount))
                # add money to second fund
                account2.get_fund(int(self._fund2_type)).change_balance(self._amount)
            else:
                print(f"Account {self._account2_number}{self._fund2_type} not found.")

            # if account.amount > self.amount:
            #     # TODO decrease account.amount by transaction._amount
            #     # TODO increase account2.amount by transaction._amount
            # else:
            #     # handling shared money market fund overdraws
            #     if account.amount > self.amount:
            #         # TODO decrease transaction._amount by account.amount
            #         # TODO set account.amount to $0
            #         # TODO decrease OTHER MM fund account.amount by self._amount
            #         # TODO increase account2.amount by self._amount
            #     else:
            #         print("You do not have enough funds.")
        #
        # if self._command_type == "H":
        #     # TODO print history
        #     print(f"Transaction History for {self._first_name} {self._last_name} by fund.")

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
        if self._fund_type:
            print("Fund Type:", self._fund_type)
        if self._amount:
            print("Amount:", f"${self._amount}")
        if self._account2_number:
            print("Account2 Number:", self._account2_number)
        if self._fund2_type:
            print("Fund2 Type:", self._fund2_type)
