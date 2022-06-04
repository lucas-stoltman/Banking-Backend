# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

class Fund:
    import decimal
    import account

    # constructor
    def __init__(self,
                 account_number: int = 0000,
                 fund_type: int = 0,
                 balance: decimal = 0):
        self._type = fund_type
        self._account_number = account_number
        self._balance = balance


    def get_type(self):
        return self._type

    def set_type(self, value: int):
        self._type = value
        return True

    def get_balance(self):
        return self._balance

    # updates the balance based on negative or positive input
    def change_balance(self, value: decimal):
        # TODO check for money market fund
        # negative balance error handling
        if self._balance + value > 0:
            self._balance += value
            return True
        else:
            print("This balance cannot become negative.")
            return False

    def display(self):
        print(f"{self._account_number}{self._type} ${self._balance}")
