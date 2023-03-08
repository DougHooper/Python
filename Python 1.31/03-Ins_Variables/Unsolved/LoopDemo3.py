# declare a variable to hold a total of numbers entered
total = 0 # accumulator / running total
number = 1 # loop control variable


# loop that allows for the user to enter numbers to add to the total
while number > 0:
     # get the input of the number
    number = int(input("\nEnter a positive number, enter 0 or a negative to stop: "))
    
    # add on to the total only if the number is greater than 0
    if number > 0:
        total += number # same as total = total + number


   # print the current total of numbers
    print(f"Current total: {total}")






