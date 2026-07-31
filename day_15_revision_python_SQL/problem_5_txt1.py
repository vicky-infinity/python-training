# --------------------------------------------------
# Q5. Library Book Records
# --------------------------------------------------

# Create a class Book.

# Attributes:
# - title
# - author
# - price

# Methods:
# - apply_discount(percent)

# Tasks:

# - Create 8 books.
# - Apply a 20% discount to every book.
# - Store books costing less than ₹350 in a dictionary
#   {title: discounted_price}.
# - Print the dictionary.


class Book():
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discout(self):
        discount = (20/100)*self.price
        return self.price - discount
    
book1 = Book("Title1","Author1",500)
book2 = Book("Title2","Author2",400)
book3 = Book("Title3","Author3",450)        
book4 = Book("Title4","Author4",350)
book5 = Book("Title5","Author5",600)


books = [book1, book2, book3, book4, book5]
discounted_books = {}
for book in books:
    newprice = book.apply_discout()
    if newprice < 350:
        discounted_books[book.title] = newprice

print(discounted_books)