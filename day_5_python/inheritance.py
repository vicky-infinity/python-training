#Class and object
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"My name is {self.name}")

    def bark(self):
        print("barking barking ")

# Child Class
class child(Animal):
    #The veriables that have mentioned into the parent class and required by the parent class that have to receve into the child class constructure and the super.__init__ as well which is parent class construtre 
    def __init__(self, name, roll):
        #Calling the parent class constructure the following is the parent class constructure
        super().__init__(name) 
        self.roll = roll
# Any of the methods can also get get the external parameters that we just have to mention in here not in the construturea and when we call the method we can use it 

    def show_roll(self):
        result = self.roll
        return result


myob = child("Ron", 88)


result = myob.show_roll()

print(result)


