# Testing purposes only, not part of the final program

from account import Account
from fund import Fund
from command_storage import CommandStorage
from transaction import Transaction

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

print("\n-------------------------------")

cmd = CommandStorage()

for i in range(cmd.get_size()):
    transaction = Transaction()
    transaction.parse(cmd.get_command())
    transaction.print_debug()
    print("\n")

