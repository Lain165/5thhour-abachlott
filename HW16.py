#Name: Austin B.
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library

#2. print "Hello World!"

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

#4. Add a and b together, then divide the sum by c. Print the result.

#5. Round the result from #3 up or down, and then determine if it is even or odd.

#6. Create a list of five different random integers between 1 and 10.

#7. Print the 4th number in the list.

#8. Append another integer to the end of the list, also random from 1 to 10.

#9. Sort the list from lowest to highest and then print the 4th number in the list again.

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.

#11. Create a list containing the names of five other students in the classroom.

#12. Create a for loop that individually prints out the names of each student in the list.

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.

#14. Free space. Do something creative. :)


import random


print('hello world')

a = int(input("give me an integer: "))
b = int(input("give me an integer: "))
c = int(input("give me an integer: "))
add1 = a + b
div1 = add1 / c
print(div1)

rou1 = (round(div1))
print(rou1)
if rou1 % 2 == 0:
    print("even")
else:
    print("odd")

list1 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
print(list1)
print(list1[3])
list1.append(random.randint(1, 10))
print(list1)
list1.sort()
print(list1)


i = 1
while i <= 100:
    print(i)
    i += 1

name = ["austin", 'ethan', 'anthony', 'wyatt', 'santi']
for name in name:
    print(name)

for numbers in range(1, 100):
    print(numbers)
    if numbers % 10 == 0:
        break

for numbers in range(1, 100):
    print(numbers)
    if numbers % 10 == 0:
        continue