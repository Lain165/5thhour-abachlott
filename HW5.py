#Name: Austin B.
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!

#1. Create a list with 5 strings containing 5 different names in it.

#2. Append a new name onto the Name List.

#3. Print out the 4th name on the list.

#4. Create a list with 4 different integers in it.

#5. Insert a new integer into the 2nd spot and print the new list.

#6. Sort the list from lowest to highest and print the sorted list.

#7. Add the 1st three numbers on the sorted list together and print the sum.

#8. Create a list with two strings, two variables, and too boolean values.

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print("hello world")

list1 = ["Austin", "Mathew", "Owen", "Ethan", "Abraham"]
print(list1)
list1.append("Coach Mac")
print(list1)
print(list1[3])
list2 = [11, 8, 200, 70]
print(list2)
list2.insert(1, 5)
print(list2)
list2.sort()
print(list2)
list2sum = list2[0] + list2[1] + list2[2]
print(list2sum)
list3 = ["hi", "bye", 1, 2, True, False]
print(list3)
list3.append(input("insert index value"))
print(list3)