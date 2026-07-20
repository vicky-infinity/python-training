# --------------------------------------------------
# Q2. Grocery Store Billing
# --------------------------------------------------

# Create a class GroceryItem.

# Attributes:
# - name
# - price
# - quantity

# Methods:
# - total_cost() → returns total cost of the item.

# Tasks:

# - Create 5 grocery items.
# - Store them in a list.
# - Calculate the grand total bill.
# - Print items whose total cost is greater than ₹500.

class GroceryItem():
    def __init__(self, name, price, qnt):
        self.name = name
        self.price =price
        self.qnt = qnt

    def total_cost(self):
        return self.qnt * self.price

my_item1 = GroceryItem("Banana",12, 12)
my_item2 = GroceryItem("Apple",120, 12)
my_item3 = GroceryItem("Cherry",4, 5)
my_item4 = GroceryItem("Kivi",200, 30)
my_item5 = GroceryItem("Jack fruit",120, 10)

itm_lst = [my_item1, my_item2, my_item3, my_item4, my_item5]

under_500 = []
grand_bill = 0
for item in itm_lst:
    grand_bill += item.price * item.qnt
    if item.total_cost() >= 500:
        under_500.append(item.name)


print(under_500)
print(grand_bill)
