# this class performs the commands it receives
class Transaction:
    import string

    _command_type = None
    _account_number = None
    _account_number2 = None
    _account_type = None
    _first_name = None
    _last_name = None
    _amount = None

    # O: Open a client account with the appropriate funds D: Deposit assets into a fund
    # W: Withdraw assets from a fund
    # T: Transfer assets between funds (can be funds owned by a single client or transfers between clients)
    # H: Display the history of all transactions for a client account or for a single fund.

    def parse(self, command: string = ""):
        self._command_type = command[0]
        print("Before", command)
        command = command[2:]
        print("After", command)

    # this function is only for testing purposes
    def print_command(self):
        print("Command Type:", self._command_type)
        print("Account Number:", self._account_number)
        print("Account Number2:", self._account_number2)
        print("Account Type:", self._account_type)
        print("First Name:", self._first_name)
        print("Last Name:", self._last_name)
        print("Amount:", f"${self._amount}")
