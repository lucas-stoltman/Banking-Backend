# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

class Accounts:

    _number = int(0)
    _type = None
    _first_name = ""
    _last_name = ""
    _balance = decimal(0)

    # Constructor
    def Accounts(self, number: int, first_name: string):

    # Setters/Getters
    def get_number(self):
        return self._number

    def set_number(self, value: int):
        self._number = value
        return True

    def get_type(self):
        return self._type

    def set_type(self, value: int):
        self._type = value
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

    # string overload
    def __str__(self):
        result = f"{self._number} {self._type} " \
                 f"{self._first_name} {self._last_name}"
        return result

    # repr overload
    def __repr__(self):
        result = f"{self._number} {self._type} " \
                 f"{self._first_name} {self._last_name}"
        return result
