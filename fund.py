# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

class Fund:
    _type = None
    _account_number = None
    _balance = decimal(0)

    # constructor
    def Fund(self, account: int, type: int, balance: decimal = 0):
        self._type = type
        self._account_number = account
        self._balance = balance
