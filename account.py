# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

class Account:
    import string
    from fund import Fund

    # Constructor
    def __init__(self,
                 account_number: int = 1000,
                 last_name: string = "Turing",
                 first_name: string = "Alan"):
        self._number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._funds = []

    # Setters/Getters
    def get_number(self):
        return self._number

    def set_number(self, value: int):
        self._number = value
        return True

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_name: string):
        self._first_name = new_name
        return True

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, new_name: string):
        self._last_name = new_name
        return True

    # functions
    def display(self):
        print(self._number, self._first_name, self._last_name)

    def find_fund(self, fund_number: int):
        if fund_number in self._funds.get_type():
            return True
        else:
            return False

    # string overload
    def __str__(self):
        result = f"{self._number} " \
                 f"{self._first_name} {self._last_name}"
        return result

    # repr overload
    def __repr__(self):
        return "{self.__class__.__name__}({self._number}, " \
               "{self._last_name}, {self._first_name})".format(self=self)
