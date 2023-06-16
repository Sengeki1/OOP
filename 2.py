class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # All Attributes
    def __init__(self, name: str, price: float, quantity = 0):
        #Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        # Assign to self object
        self.nameVar = name
        self.priceVar = price
        self.quantityVar = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.priceVar * self.quantityVar
    
    def apply_discount(self):
        self.priceVar = self.priceVar * self.pay_rate # Overite the attribute of price

    def __repr__(self):
        return f"Item('{self.nameVar}', {self.priceVar}, {self.quantityVar})"

# Instances 
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.nameVar)
