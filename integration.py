# Create a class Calculator with self.history = [] in __init__.
class Calculator:
    
    def __init__(self):
# Store all operation rows in self.history.
        self.history = []
        self.result = 0

# Add methods add(x, y) and subtract(x, y) that return results.
# In each method, store a string in history like "8 - 3 = 5".
    def add(self,x,y):
        self.result = x + y
        self.history.append(f'{x} + {y} = {self.result}')
        return self.result
        
    def subtract(self,x,y):
        self.result = x - y
        self.history.append(f'{x} - {y} = {self.result}')
        return self.result
    
# Extend Calculator with methods multiply(x, y) and divide(x, y).
# In divide, if y == 0, store "Cannot divide by zero" in history and return None.
    def multiply(self,x,y):
        self.result = x * y
        self.history.append(f'{x} * {y} = {self.result}')
        return self.result
    
    def divide(self,x,y):
        if y == 0:
            self.history.append('Cannot divide by zero')
            return None
        else:
            self.result = x / y
            self.history.append(f'{x} / {y} = {self.result}')
            return self.result
    
# Add method show_history() that prints all rows in self.history.
    def show_history(self):    
        for row in self.history:
            print(row)

# Add method clear_history() that removes all history rows.
    def clear_history(self):    
            self.history.clear()

# Create one calculator object.
calc = Calculator()

# Test this order: add, divide by zero, multiply, show history, clear history, show history again.
print(calc.add(4, 7))
print(calc.divide(4, 0))
print(calc.multiply(1, 2))

print("\n--- History ---")
calc.show_history()

calc.clear_history()

print("\n--- After clear ---")
calc.show_history() 

