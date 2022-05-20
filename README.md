# Banking-Backend

The backend of a banking interface that tracks user accounts.

The user accounts are stored in a binary search tree structure, and the commands are passed in through a queue.

The user can:

  - Open a client account with the appropriate funds 
  - Deposit assets into a fund
  - Withdraw assets from a fund
  - Transfer assets between funds (can be funds owned by a single client or transfers between clients)
  - Display the history of all transactions for a client account/fund
