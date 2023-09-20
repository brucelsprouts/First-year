#Activity 5: coffee
drink_order = input("What would you like to drink? (coffee or other): ")

if drink_order.lower() == "coffee":
    customer_age = int(input("How old are you? "))
    if customer_age >= 10:
        print("Here's your coffee. Enjoy!")
    else:
        print("I'm sorry, but you must be 10 years or older to order coffee.")
else:
    print(f"Here's your {drink_order}. Enjoy!")
