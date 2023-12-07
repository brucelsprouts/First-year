# Product class for defining product attributes and methods
class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are compared for equality
    def __eq__(self, other): 
        if isinstance(other, Product):
            return (
                self._name == other._name and 
                self._price == other._price and 
                self._category == other._category
            )
        return False

    # Getter methods for product attributes
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # String representation of a product
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep
        
    # Ensure instances of 'Product' can be used as elements in a set within the 'ProductCatalog' class
    def __hash__(self):
        return hash((self._name, self._price, self._category))

# Inventory class managing product inventory
class Inventory:
    # Initialize an empty inventory dictionary
    def __init__(self):
        self._inventory = {}

    # Method to add products to the inventory
    def add_to_productInventory(self, productName, productPrice, productQuantity):
        self._inventory[productName] = {'price': productPrice, 'quantity': productQuantity}

    # Methods to modify product quantity in the inventory
    def add_productQuantity(self, nameProduct, addQuantity):
        self._inventory[nameProduct]['quantity'] += addQuantity

    def remove_productQuantity(self, nameProduct, removeQuantity):
        # Check if requested quantity is available, if not, display a message
        if self._inventory[nameProduct]['quantity'] >= removeQuantity:
            self._inventory[nameProduct]['quantity'] -= removeQuantity
        else:
            print("Requested quantity exceeds what is available in the inventory.")

    # Getter methods for product price and quantity
    def get_productPrice(self, nameProduct):
        return self._inventory[nameProduct]['price']

    def get_productQuantity(self, nameProduct):
        return self._inventory[nameProduct]['quantity']

    # Display the entire inventory
    def display_Inventory(self):
        for product, details in self._inventory.items():
            print(f"{product}, {details['price']}, {details['quantity']}")

# ShoppingCart class handling shopping operations
class ShoppingCart:
    def __init__(self, buyerName, inventory):
        self._buyerName = buyerName
        self._cart = {}
        self._inventory = inventory

    # Method to add products to the shopping cart
    def add_to_cart(self, nameProduct, requestedQuantity):
        if self._inventory.get_productQuantity(nameProduct) >= requestedQuantity:
            if nameProduct in self._cart:
                self._cart[nameProduct] += requestedQuantity
            else:
                self._cart[nameProduct] = requestedQuantity
            self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
            return "Filled the order"
        else:
            return "Can not fill the order"

    # Method to remove products from the shopping cart
    def remove_from_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self._cart:
            return "Product not in the cart"
        elif self._cart[nameProduct] < requestedQuantity:
            return "The requested quantity to be removed from cart exceeds what is in the cart"
        else:
            self._cart[nameProduct] -= requestedQuantity
            self._inventory.add_productQuantity(nameProduct, requestedQuantity)
            return "Successful"

    # View the items in the shopping cart along with the total price
    def view_cart(self):
        total_price = 0
        for product, quantity in self._cart.items():
            price = self._inventory.get_productPrice(product)
            total_price += price * quantity
            print(f"{product} {quantity}")

        print(f"Total: {total_price}")
        print(f"Buyer Name: {self._buyerName}")

# ProductCatalog class managing a collection of products
class ProductCatalog:
    def __init__(self):
        self._catalog = set()
        self._low_prices = set()
        self._medium_prices = set()
        self._high_prices = set()

    # Method to add products to the catalog
    def addProduct(self, product):
        self._catalog.add(product)

    # Categorize products based on their price
    def price_category(self):
        for product in self._catalog:
            price = product.get_price()
            if price <= 99:
                self._low_prices.add(product)
            elif 100 <= price <= 499:
                self._medium_prices.add(product)
            else:
                self._high_prices.add(product)

        print(f"Number of low price items: {len(self._low_prices)}")
        print(f"Number of medium price items: {len(self._medium_prices)}")
        print(f"Number of high price items: {len(self._high_prices)}")

    # Display the entire product catalog
    def display_catalog(self):
        sorted_catalog = sorted(self._catalog, key=lambda x: (x.get_price(), x.get_name(), x.get_category()))
        for product in sorted_catalog:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")


# Non-class functions for populating inventory and catalog
# Function to populate the inventory from a file
def populate_inventory(filename):
    inventory = Inventory()
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                inventory.add_to_productInventory(data[0], int(data[1]), int(data[2]))
    except FileNotFoundError:
        print(f"Could not read file: {filename}")
    return inventory

# Function to populate the product catalog from a file
def populate_catalog(fileName):
    catalog = ProductCatalog()
    try:
        with open(fileName, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(data[0], int(data[1]), data[3])
                catalog.addProduct(product)
    except FileNotFoundError:
        print(f"Could not read file: {fileName}")
    return catalog
