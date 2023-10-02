IDEAL_CREDIT_SCORE = 720 

userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the hosue: "))

if userScore >= IDEAL_CREDIT_SCORE: #Change => to >= (syntax error)
    downPayment = 0.1 * housePrice
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600: #Changes else if to elif and remove
    downPayment = 0.2 * housePrice                       #quotes around 600 (syntax and logic error)
else:
    downPayment = 0.3 * housePrice #Indent line to under the else staement (indentation error)

print("Your down payment is: ${}".format(downPayment)) #Replaced "()" with "{}" (logic error)

"""
IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the hosue: "))

if userScore => IDEAL_CREDIT_SCORE:
    downPayment = 0.1 * housePrice
else if userScore < IDEAL_CREDIT_SCORE and userScore > "600":
    downPayment = 0.2 * housePrice
else:
downPayment = 0.3 * housePrice

print("Your down payment is: $()".format(downPayment))
"""