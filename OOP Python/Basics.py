class Item:     # Define class
    def calculate_total_price(self, x, y):          # This is a method as it is within a class
        return x * y

item1 = Item()              # Each parameter is added to item1 rather than as separate variables, so item1 contains name
item1.name = "Phone"                                                                            # price and quantity
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))     # Prints result of price * quantity
