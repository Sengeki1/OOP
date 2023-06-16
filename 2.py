class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity = 0):
        #Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        # Assign to self object
        self.nameVar = name
        self.priceVar = price
        self.quantityVar = quantity

    def calculate_total_price(self):
        return self.priceVar * self.quantityVar
    
    def apply_discount(self):
        self.price *= Item.pay_rate # Overite the attribute of price

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for instance level