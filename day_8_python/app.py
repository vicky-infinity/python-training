class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        result = self.price * 10 /100
        return result
    
ob1 = Product("Keyboard",600)
ob2 = Product("Mouse",300)
ob3 = Product("Monitor",800)
ob4 = Product("Webcam",450)

print(ob1.apply_discount())