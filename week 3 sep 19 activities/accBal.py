# Activity 2: accBal
bal = int(input("please enter your balance: "))
withdraw = int(input("please enter how much you would like to withdraw: "))

if bal >= withdraw:
    bal = bal - withdraw
    print("Withdrawal successful! Your new balance is: " + str(bal))
else:
    print("Insufficient funds. Withdrawal not possible.")
