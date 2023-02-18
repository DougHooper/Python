'''
    Data in programming languages can be 
    literal
'''
print(15) # displays the integer literal value of 15
print(15.55) # displays the float / double literal value of 15.55
print('C') # displays the string literal for the letter C
print("Bootcamp") #displays the string literal for the text Bootcamp
print(False) # display the boolean literal for the value False


'''
    Data in programming languages can be sotered in variables

    ' variable declaration in VB: Dim varName As DataType
    ' variable declaration in Python: varName = value
'''
num1 = 15 # stores an integer value in a variable named num1
num2 =15.55 # stores a float value in a variable name num2
text1 = 'C' # stores an string value in a variable named text 1
text2 = "Bootcamp" # stores an string value ni a variable named text 2
flag = False # stores a boolean value in a variable named flag

# display the outputs of the variables
print("num1 =" + str(num1)) #str() converts the integer to a string and adds to output
print("num1 =" + str(num2)) #str() converts the float to a string and adds to output
print("num1 =" + text1) #str() converts the integer to a string and adds to output
print("num1 =" + text2)
print("num1 =" + str(flag)) # str() converts the boolean to a string and adds to output


print(f"num1 = + str{num1}, text1 = {text1}") # formatted string of output
# if data has '' or "" outter part of double string has to be double and single on inner or vice versa
