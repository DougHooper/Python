'''
    in order to do input, use the input() function
    
    input contains 2 parts:
        1. prompt
        2. input

    set variable = result of calling the input function

    by default, the input functino stores strings

    user the presses enter key which can be stored into a variable which can be used later on
'''

name = input("Please enter your name: ")

print(f"Hello {name}!") # displays the value of name

# convert the value of our meetingNumber to an integer
meetingNumber = int(input("How many bootcamp class meetings have been held? "))

# output of our data
print(f"So far, we have met {meetingNumber} times.")
print(f"Next class, will be meeting #{(meetingNumber+1)}.")

# need to convert the input to an interger if you want to do a numeric calculation
# put the variable in the curly brackets around parenthesis to do a calculation

