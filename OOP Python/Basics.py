import csv  # needed to read csv

class Item:     # Define class
    #Class attributes, these are set for all instances
    pay_rate = 0.8  # Creating a class attribute
    # Due to code in __init__, everytime an intstance created, its details are added here
    all = []
    def __init__(self, name: str, price: float, quantity=0): # When an objet is initialised, this runs
        # This creates instance attributes
        # The extra parameters created give the object these required attributes
        # quantity=0, sets a default value for if none is given
        # name: str means that name can only accept strings
        # So class Item now requires name, price and quantity when initialised


        # Run validations on attributes given, if false it gives the error message
        # So if  price = -10, gives error message "Price -10 is not >= 0"
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0"


        # These are instance attributes
        #   Assign to self to make attributes callable
        self.name = name
        self.price = price
        self.quantity = quantity


        # Adds instance to class attribute "all"
        Item.all.append(self)


    def calculate_total_price(self):          # This is a method as it is within a class
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate


    # Creating a class method
    @classmethod
    def instantiate_from_csv(cls):
        # How to instantiate from cs file
        with open("items.csv", "r") as f: # use with instead of normal open as it auto closes when done
            reader = csv.DictReader(f)
            items = list(reader)    # Creates list of dictionaries
        # Each dict is used to create an item
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity"))
            )

    # Creating static method
    @staticmethod
    def is_integer(num):
        # Count out .00 numbers
        if isinstance(num, float):  # Checks if a float
            return num.is_integer() # This counts out .00
        elif isinstance(num, int):
            return True
        else:
            return False
    # This means that when print instance, it returns what is given
    # Rather than memory address
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    # self.__class__.__name__ gives the name of the class, or of the child class of the parent it is used in

# Without __init__ you need to do this
#item = Item()              # Each parameter is added to item1 rather than as separate variables, so item1 contains name
#item.name = "Phone"                                                                            # price and quantity
#item.price = 100
#item.quantity = 5
#print(item1.calculate_total_price(item1.price, item1.quantity))     # Prints result of price * quantity


# With __init__ you can do this
#item = Item("Phone", 100, 5)     # This creates instance attributes
# You can still add your own attributes to each specific object
#item.has_numpad = False


# Calling a class attribute
#print(item.pay_rate)   # First it checks if any instance attributes match
                        # Then it checks for any class attributes 2nd


# Magic attribute to give all attributes
#print(Item.__dict__)  # Prints all class attributes as a dictionary
#print(item.__dict__)  # Prints all instance attributes as a dict


# How to change a class attribute
#item.pay_rate = 0.7
#item.apply_discount()
#print(item.price)


#item1 = Item("Phone", 100, 1)
#item2 = Item("Laptop", 1000, 3)
#item3 = Item("Cable", 10, 5)
#item4 = Item("Mouse", 50, 5)
#item5 = Item("Keyboard", 75, 5)


#for instance in Item.all:   # How to iterate through "all" attribute
#    print(instance.name)    # To access specific attribute for all instances


#print(Item.all)     # Now it prints in format specified by __repr__


# How to instantiate from a csv
Item.instantiate_from_csv()

# Inheritance

# Creating a new class that inherits features of the Item class
# Now Item is a parent clas and this is a child class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity           # This gives full access of the attributes in parent class
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not >= 0"

        self.broken_phones = broken_phones

phone1 = Phone("jscPhone", 500, 5, 1)
print(Item.all) # phone1 is still counted as part of this
