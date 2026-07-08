# These are the special methods when we call in these mathod, by default it returns the computer memory address of the object 
# for example if we do myab = class(parms) /n print(myob) then it will return "<__main__.test object at 0x0000023566578590>"

class test():
    def __init__(self, book, pages, author):
        self.book = book
        self.pages = pages
        self.author = author
    
    def total_pages(self):
        cnt = self.pages+2
        return cnt
    
    # this str special method if used when someone print print the object
    def __str__(self):
        result = f"{self.author}: This is the author"
        return result
    
    # This len special method is used when someone trys trys to check or print the len of the object
    # This len method only return the integer 
    def __len__(self):
        result = self.pages
        return result
    
    # This special method is to delete the object of the clas
    def __del__(self):
        return "The object is deleted"
    
ob = test("law of power", 100, "xyz")

print(ob)
print(len(ob))





