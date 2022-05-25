# Testing purposes only, not part of the final program

from account import Account
from fund import Fund

acc = Account()

acc.get_number()

# __str__ overload
print(str(acc))

# __repr__ overload
print(repr(acc))

print("\n-------------------------------")

# default
fund1 = Fund()
fund1.display()

# custom
fund2 = Fund(acc.get_number(), 3, 69)
fund2.display()
