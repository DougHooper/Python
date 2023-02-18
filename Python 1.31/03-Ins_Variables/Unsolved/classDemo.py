# display the literal value of 1.2345 to the console
print(1.2345)

# store the value of "Python" into a variable named topic
topic = "Python" #could also use single quotes

# store the value of 3 into a variable named unit
unit = 3

# store a value that is one more than the value of unit into a variable named nextUnit
nextUnit = unit + 1

"""
    arithmetic in Python
    + addition
    - subtraction
    * multiplication
    / division
    
    in VB, we used mod for modular division
    in python, use % symbol for modular division

    modular division = what the remainder is after you do a division

    4 / 2 = 2 (evenly divisibly by 4)
    4 % 2 = 0 (so whatever would be left over)

"""

# using a regular print statement, display the following output
# "Module 3 is our Python Unit" (where 3 is in unit, and Python is in 'topic')

print("Module " + str(unit) + " is our " + topic + " Unit")

# using a formatted string print statement, display the following output
# "Module 3 is our Python Unit" (where 3 is in unit, and Python is in 'topic')
print(f'Module {unit} is our {topic} Unit')