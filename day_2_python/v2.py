# Version Second


class info:
    def __init__(self,name:chr,age:int,phone,city,pin,roll,marks):
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city
        self.pin = pin
        self.roll = roll
        self.marks = marks


    def greet(self):
            print("Hey", self.name)

    def comb(self):
         return print(self.name,"This is the greetings function ",self.roll)

ob1 = info("vicky",40,7878909890,"HYD",443234,105001,87)

print(ob1.city)
ob1.greet()


print(ob1.greet())


