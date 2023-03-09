# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# print out items

for candy in candy_list: 
    print(f"{candy_list.index(candy)} - {candy}")


for treat in range(allowance):
    choice = int(input("Enter the number of the candy you want: "))

    # validating input
    while(choice < 0 or choice > len(candy_list)-1):
        print("\nERROR: Invalid Choice try again")
        choice = int(input("Enter the number of the candy you want: "))

    candy_cart.append(candy_list[choice])

print("\nMy Candy Cart Contains......")
for candy in candy_cart:
    print(candy)