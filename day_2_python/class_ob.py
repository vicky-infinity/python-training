# Basics of Class and Objects


class info:
    # Class constructor
    def __init__(self,name,age,phone,city,pin,roll,marks):
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city
        self.pin = pin
        self.roll = roll
        self.marks = marks


    def greet(self):
            print("Hey: ", self.name)

    def comb(self):
         print(self.name," ",self.roll)

s1 = info("vicky",1,1,1,1,10569,1)

print(s1.comb("vicky", 198400))
        

