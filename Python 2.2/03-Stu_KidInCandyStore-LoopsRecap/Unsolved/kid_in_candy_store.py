# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []


# Print out options
for candy in candy_list:
    # use listName.index(item) to grab the index of an item from a list
    print(f"{candy_list.index(candy)} - {candy}")


# allow the user to choose candy based on the allowance
print("Enter the numbers of the candy that you would like to choose: ")
for treat in range(allowance):
    choice = int(input(f"You have {allowance - (treat)} choices left. \nEnter the number of the candy you want: "))


    # validating input
    while(choice < 0 or choice > len(candy_list)-1):
        print("\nERROR: Invalid Choice try again")
        choice = int(input("Enter the number of the candy you want: "))


    # add the candy to the cart
    candy_cart.append(candy_list[choice])


# once I am out of allowance, display the candy chosen in the cart
print("\nMy Candy Cart Contains......")
for candy in candy_cart:
    print(candy)