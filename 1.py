class Item:
    pass

item1 = Item() # Instance/ Object
# Attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) # str
print(type(item1.name)) # int
print(type(item1.price)) # int
print(type(item1.quantity)) # int