"""
    basic for loop structure
​
        for variable in range():
            statement(s)
​
    when range(single number) - loop starts at 0 and repeats number - 1
    when range(start, finish) - loop starts at start and repeats until finish - 1
    when range(start, finish, increment) - loop starts at start and repeats until finish-1 and increments by the third value
"""
#for x in range(10):
#    print(x) # displays 0 - 9 on separate lines


#for x in range(5, 20):
#    print(x) # displays 5 - 19 on separate lines    


#for x in range(1, 20, 2):

#    print(x) # displays 1 - 19 odd numbers on separate lines 



"""
    you can also use for loops to iterate through lists
"""


list1 = ["alpha", "beta", "gamma", "delta"]


"""
    for item in list:
        do something with the specific item in the list
"""

#for item in list1:
#    print(item) # displays each item on separate lines


#for i in range(len(list1)):
#    if i < 2:
#        print(list1[i]) # displays the first two items from the list

#for item in list1:
#    if len(item) == 5: #checks for the length of the characters in the string

#        print(item) # displays each item on separate lines


# strings are lists of characters
#feeling = "HAPPY"


#for letter in feeling:
#    print(letter) # prints each letter on separate lines


for item in list1:
    if len(item) == 5: #checks for the length of the characters in the string
        print(item)
        print("*******************")
        for letter in item:
            print(letter) # prints each letter of each word that is 5 characters on separate 