# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from account import Account
from fund import Fund
from command_storage import CommandStorage
from transaction import Transaction
from account_storage import Node, BST

# initializing the BST
storage = BST()
if __name__ == "__main__":

    # 1) The program will read in a string of transactions from a file into an in-memory queue.
    cmd = CommandStorage()

    # 2) The program will next read from the queue and process the transactions in order.
    for i in range(cmd.get_size()):
        transaction = Transaction()
        command = cmd.get_command()
        print(command)
        transaction.transact(command)
        # transaction.print_debug()

    # TODO while queue !empty
    #   process first command

    # TODO When the queue has been
    #  depleted the program will print
    #  out all open accounts and balances
    #  in those accounts.
