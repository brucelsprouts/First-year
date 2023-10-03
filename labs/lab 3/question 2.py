# Initialize the accountTotal variable with $50
accountTotal = 50

#Loops from 50 to 20
while accountTotal > 20: #Changed =< to > since >= would make the balance go down to 19 at the end of the program
    #Prints current account total
    print(accountTotal)

    #Decrements accountTotal by 1$ every print
    accountTotal -= 1

#Print message when account has reached 20$
print('Your account has reached $20.')