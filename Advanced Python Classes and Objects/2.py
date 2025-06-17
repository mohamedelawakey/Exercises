""" 

Exercise 2: Magic Methods (str and repr) Instructions:

Create a Book class with attributes like title, author, and pages.
Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'"{self.title}" by {self.author} with ({self.pages} of pages)'
    
    def __repr__(self):
        return f'title: {self.title}", author: {self.author}, pages: ({self.pages})'

book =  Book('1984', '', 400)
print(book)