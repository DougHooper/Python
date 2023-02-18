"""
    while loops are pretest loops
    
    checks for the condition first, then loop if the condition is true
    
    structure:
    
        while condition:
            statement(s)
            
    ** AT LEAST ONE statement needs to update the condition **
    ** if not, you can create an infinite loop!! **
    
    While loops can execute from 0 up to as many times as needed
"""
# loop control variable
repeat = 3 # variable controls the loop that is defined below
# while loop example

while repeat > 0:
    # checks to see if the value of repeat is greater than 0
    print("This is a python loop")

   # update the value of repeat
    # repeat = repeat - 1 # subtracts 1 from repeat on each pass

  # combined assignment operator
    repeat -= 1 # same as repeat = repeat - 1
    # can also be used with +=, *=, /=, and %= (can only be used with ints)