class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    def addItem(self, price):  # Added 'self' parameter
        self._itemCount += 1
        self._totalPrice += price 
        
    def clear(self):  # Removed unnecessary 'total' parameter
        self._itemCount = 0
        self._totalPrice = 0.0

    def getTotal(self):  # Removed unnecessary 'total' parameter
        return self._totalPrice 
    
register = CashRegister()

register.addItem(5.0)
register.addItem(3.5)

total_price = register.getTotal()
print("Total Price:", total_price)

register.clear()
total_price = register.getTotal()
print("Total Price after clearing:", total_price)