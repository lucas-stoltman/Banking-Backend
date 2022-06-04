# Testing purposes only, not part of the final program

from account import Account
from fund import Fund
from command_storage import CommandStorage
from transaction import Transaction
from account_storage import Node, BST

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

# --- transaction testing ---
# print("\n---\033[1m", "transaction testing", "\033[0m---", )
#
# cmd = CommandStorage()
#
# for i in range(cmd.get_size()):
#     transaction = Transaction()
#     transaction.parse(cmd.get_command())
#     transaction.print_debug()
#     print("\n")

# Node Testing
print("\n---\033[1m", "Node Testing", "\033[0m---", )

acc = Account()
node = Node(acc.get_number(), acc)
print(node)

acc1 = Account(5231, "Smith", "John")
node1 = Node(acc1.get_number(), acc1)
print(node1)

acc2 = Account(2222, "Mraz", "Jason")
node2 = Node(acc2.get_number(), acc2)
print(node2)

acc3 = Account(5555, "Punk", "Daft")
node3 = Node(acc3.get_number(), acc3)
print(node3)


# BST Testing
print("\n---\033[1m", "BST Storage Testing", "\033[0m---", )
storage = BST()

# put
print("--Put testing--")
print(storage.put(node.key, node))
print(storage.put(node1.key, node1))
print(storage.put(node2.key, node2))
# attempt to place duplicate in
print(storage.put(node.key, node))

# get
print("\n--Get testing--")
print(storage.get(node.key))
print(storage.get(node1.key))
print(storage.get(node2.key))
# this one hasn't been placed in the bst
print(storage.get(node3.key))


