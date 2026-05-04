# Create a class Car with attributes brand and year.

class Car: 
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def show_info(self):
        print(f"Brand: {self.brand}, year: {self.year}")

# Create one car object and print its brand.
car_1 = Car("Honda",1991)

# Add method show_info() that prints both attributes.
car_1.show_info()

# Create class Counter with attribute value starting at 0.
class Counter:
    value = 0
    def __init__(self):
        pass
# Add method increase() that adds 1 to value.
    def increase(self):
        self.value +=1 
    
# Call increase() twice and print value.
count = Counter()
count.increase()
count.increase()
print(count.value)

# Create a class Book with title and pages.
class Book:
    long_book = False
    def __init__(self, title,pages):
       self.title = title
       self.pages = pages
       
# Add method is_long() that returns True if pages are over 300.
    def is_long(self):
          return self.pages > 300
# Add method summary() that prints title and pages.
    def summary(self):
        print(f'Title: {self.title}, {self.pages} pages')

# Create two books and test both methods.
first_book = Book("Title", 700)
second_book = Book("Second Title", 1100)
first_book.summary()
print(Book.is_long(second_book))