'''
def greet(name):
    print(f"Hello, {name}!")
    
greet("Alice")

def add(a, b):
    return a + b

results = add(2, 5)
print(f"The result is: {results}")
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
greet("phillip", "Good morning")