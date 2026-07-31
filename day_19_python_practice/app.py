
# --------------------------------------------------
# Q6. Restaurant Menu
# --------------------------------------------------

# Create a class FoodItem.

# Attributes:
# - item_name
# - price
# - category

# Methods:
# - is_affordable() → returns True if price is below ₹250.

# Tasks:

# - Create 6 food items.
# - Store them in a list.
# - Print the names of all affordable food items.
# - Also print the total number of affordable items.

class FoodItem():
    def __init__(self,item_name, price, category):
        self.item_name = item_name
        self.price = price
        self.category = category

    def is_affordable(self):
        if self.price < 250:
            return True
        else:
            return False

item1 = FoodItem("mango",250,"Frout")
item2 = FoodItem("apple",350,"Frout")        
item3 = FoodItem("cherry",120,"Frout")
item4 = FoodItem("milk",150,"dairy")
item5 = FoodItem("eggs",200,"dairy")
item6 = FoodItem("rise",500,"pulses")


myitms = [item1,item2, item3, item4, item5, item6]

myitems = {}
total_cost = 0
for item in myitms:
    if item.is_affordable() == True:
        myitems[item.item_name] = item.price
        
        total_cost += item.price
print(myitems)
print(total_cost)



# --------------------------------------------------
# Q7. Mobile Phone Store
# --------------------------------------------------

# Create a class Mobile.

# Attributes:
# - brand
# - model
# - price

# Methods:
# - apply_discount(percent)

# Tasks:

# - Create 5 mobile phones.
# - Apply a 10% discount.
# - Build a dictionary {model: final_price} for mobiles whose final price is above ₹20,000.
# - Print the dictionary.


# --------------------------------------------------
# Q8. Hospital Patient Records
# --------------------------------------------------

# Create a class Patient.

# Attributes:
# - patient_id
# - name
# - age

# Methods:
# - is_senior() → returns True if age is at least 60.

# Tasks:

# - Create 7 patients.
# - Store all patients in a list.
# - Print names of all senior citizens.
# - Print the total number of senior citizens.


# --------------------------------------------------
# Q9. Online Course Portal
# --------------------------------------------------

# Create a class Course.

# Attributes:
# - title
# - duration
# - fee

# Methods:
# - is_long_course() → returns True if duration is greater than 25 hours.

# Tasks:

# - Create 6 courses.
# - Store them in a list.
# - Build a dictionary
#   {course_title: duration}
#   for long-duration courses.
# - Print the dictionary.


# --------------------------------------------------
# Q10. Vehicle Service Center
# --------------------------------------------------

# Create a class Vehicle.

# Attributes:
# - owner_name
# - vehicle_number
# - service_cost

# Methods:
# - add_service_charge(amount)

# Tasks:

# - Create 6 vehicles.
# - Add a service charge of ₹500 to every vehicle.
# - Print details of vehicles whose final service cost exceeds ₹4000.
# - Also print the total service revenue.