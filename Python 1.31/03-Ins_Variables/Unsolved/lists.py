# declare two listss
myList1 = ["jim", "james", "paul", "tyrone"]
myList2 = [15, 30, 35, 40]
myList = ["A", 90, "B", 80]
myList3 = ["A", 90, "B", 80]

# display all of the contents of a list
print(myList1)

# display one item from a list
print(myList1[0]) # display the value of index 0
print(myList2[0]) # display the value of index 0
print(myList3[0]) # display the value of index 0

# use len() to display the size (# of items in a list)
print(len(myList1))

#use .append() to add items to a list
myList1.append("Andre")
myList1.append("Erykah")

print(myList1) #print the updated list

# use .remove() to remove a specific item
myList1.remove("Erykah")
print(myList1) # print the updated list

# use.pop() to add and remove items based on an index value
myList1.pop(0) # removing the current value at index 0
print(myList1) #print the updated list

# to add a value at a new index using .insert()
myList1.insert(4, "Erykah is Back")
myList2.insert(2, "Jay")
print(myList1) # print the updated list