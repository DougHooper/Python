# while loops can also be used to validate input
repeat = int(input("Enter a value that is between 1 and 3: " ))


# when validating, use the while loop to check for bad data
# in this case, only loop when the value entered is less than 1 or greater than 3
while repeat < 1 or repeat > 3:
    # display an error message
    print("\nERROR: Number is out of range, try again\n" 
          "\nerror error\n")
    # get another value of repeat
    repeat = int(input("Enter a value that is between 1 and 3: "))

# once valid data is entered, execute the loop
while repeat > 0:
    # checks to see if the value of repeat is greater than 0
    print("This is a python loop")
    repeat -= 1 # same as repeat = repeat - 1. When udpating the value of your variable. 









