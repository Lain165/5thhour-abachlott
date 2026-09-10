#Name:Austin B.
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.

#2. Sort the list from highest to lowest.

#3. Create an empty list.

#4. Remove the median number from the first list and add it to the second list.

#5. Remove the first number from the first list and add it to the second list.

#6. Print both lists.

#7. Add the two numbers in the second list together and print the result.

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

#9. Sort the first list from lowest to highest and print it.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
list1.sort(reverse=True)
print(list1)
list2 = []
print(list2)
list1.remove(5)
list2.append(5)
list1.remove(1)
list2.append(1)
print(list1)
print(list2)
list2sum = sum(list2)
print(list2sum)
list2.remove(1)
list2.remove(5)
list1.append(6)
print(list2)
list1.sort(reverse=False)
print(list1)