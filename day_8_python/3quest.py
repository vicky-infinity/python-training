# Q3. Rectangle
# Create a class Rectangle:

# attributes: length, width
# method area()

# Create a list of rectangles and print areas > 50.

class Rectangle():

    countrect =[]

    def __init__(self,len,wid):
        self.len = len
        self.wid = wid

    def area(self):
        area = self.len * self.wid
        self.countrect.append(area)

    def checklist(self):
        return self.countrect
    
myob = Rectangle(40,40)

myob.area()
print(myob.checklist())



        
        
        
