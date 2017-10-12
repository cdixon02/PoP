'''This function computes the square of a number and prints it out'''
def square(x): # procedure - has side effects
    print(x*x)    

square(3)
square(5)
square(-10)
    
def square(x): # fruitful function - returns the value
    #pass
    return x * x

assert square(3) == 9
assert square(5) == 25
assert square(-10) == 100
