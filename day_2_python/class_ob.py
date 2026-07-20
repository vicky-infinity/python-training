# Basics of Class and Objects


class info:
    # Class constructor
    def __init__(self,name,age,phone,city,pin,roll,marks):
        # These are the attributes 
        # We can access the attributes with using dot like object.attribut example ob1.name and it will print the attribute value        self.name = name
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city
        self.pin = pin
        self.roll = roll
        self.marks = marks


    def greet(self):
            print("Hey Good morning: ", self.name)

    def comb(self):
         print(self.name," ",self.roll)

s1 = info("vicky",1,1,1,1,10569,1)

print(s1.comb("vicky", 198400))
        

