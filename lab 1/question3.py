#Prompt for shop name
shopName = input("Please enter the shop name: ")

#Ask user for QTY of ring and glasses
ringQTY = int(input("Please enter ring QTY: "))
glassesQTY = int(input("Please enter glasses QTY: "))

#Display known information on shopName, ringQTY, and glassesQTY
print("shop name i s {}".format(shopName))
print("Ring QTY is {}".format(ringQTY))
print("Glasses QTY is {}".format(glassesQTY))

#Display total number of items (ringQTY and glassesQTY)
print("Inventory total: {}".format(ringQTY+glassesQTY))