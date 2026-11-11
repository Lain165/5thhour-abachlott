#Name: Austin B.
#Class: 5th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.

#4. Create a for loop that prints 5 different animals from a list.

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

#6. Create a list containing 10 integers of your choice and print the list.

#7. Create two empty variables named evenNumbers and oddNumbers.

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.



#9. Create a variable that asks the user for an integer and an empty integer variable.

#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)


import math

for i in range(5, 0, -1):
    print(i)
else:
    print("hello world")

for l in range(0, 30, 2):
    print(l + 2)

for n in range(0, 30, 1):
    if n % 3 == 0:
        continue
    print(n)

animals = ["dog", "cat", "mouse", "rabbit", "horse"]
for n in animals:
    print(n)

for n in "Austin"[::-1]:
    print(n)


num = (1, 209, 222, 27, 64, 76, 898, 889, 160, 100)
print(num)
evenNumbers = []
oddNumbers = []

for n in num:
    if n % 2 == 0:
        evenNumbers.append(n)
    if n % 2 == 1:
        oddNumbers.append(n)

print(evenNumbers)
print(oddNumbers)

i = int(input("give me an integer: "))

for n in range(1, i+1):
    i *= n
    print(i)

