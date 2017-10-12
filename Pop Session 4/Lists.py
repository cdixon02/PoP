numbers = [1,2,3]
print(numbers)
for i in range(len(numbers)):
    numbers[i] = numbers [i] * 2
print(numbers)
more_numbers = [4,5,6]
cheese = numbers + more_numbers
print(cheese)
new_numbers = [1,2,3,4,5,6]

print(new_numbers[2:4])
new_numbers[1:2] = ['x', 'y']
print(new_numbers)

# The list method append adds a new element to the end of a list.
new_numbers.append(23)
print(new_numbers)

#The list method extend takes a list as an argument and appends all of the elements:
#(QUESTION - is the list extend the same as a += b?)
new_numbers.extend(numbers)
print(new_numbers)

#The list method sort arranges the elements of th list from low to high:
pikachu = [2,1,5]
pikachu.sort()
print(pikachu)

##This function creates a temporary variable which loops through the list you 
##have fed into it and returns the total amount 
def add_all(t):
    total = 0 #The variable 'total' in this example is sometimes referred to as an accumulator.
    for x in t:
        total += x
    return total
print(add_all(pikachu))
##Sum does the same thing for lists/arrays and is a built-in function.
print(sum(pikachu))
a = [1,2,3,4,5]
print(sum(a))
##This function takes a list and capitalizes its contents in the return.
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
woof = "woof"
print(capitalize_all(woof))
##A function which returns a new list that contains only the upper case characters of a string
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
charmander = "ChArMaNdEr"
print(only_upper(charmander))
