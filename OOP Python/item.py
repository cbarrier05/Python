class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0"
        self.__name = name       # Makes it read only after initialisation
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):             # Call the read only attribute
        return self.__name

    @name.setter                # Allows you to set the name to anything
    def name(self, value):
        if len(value) >= 10:
            self.__name = value

    # @property
    # def name(self):         # This won't work for an existing attribute such as name
    #    return self.name

    def calculate_total_price(self):
        return self.price * self.quantity

    def __apply_discount(self):     # The __ makes it a private method that can't be called outside the class
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    # @property
    # def read_only_name(self):       # This has created a read only attribute, can't be edited, and its value is "AAA"
    #    return "AAA"
