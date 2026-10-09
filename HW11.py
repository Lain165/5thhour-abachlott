#Name: Austin B.
#Class: 5th Hour
#Assignment: HW11


#1. Print "Hello World!"

#2. Create a list with three variables that each randomly generate a number between 1 and 100

#3. Print the list.

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

print("Hello World")
import random
Var1 = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]
print(Var1)
if Var1[0] >= Var1[1] and Var1[0] >= Var1[2]:
    num = Var1[0]
elif Var1[0] >= Var1[1] and Var1[0] >= Var1[2]:
    print("first number is greatest")
    num = Var1[1]
elif Var1[1] >= Var1[2] and Var1[1] >= Var1[0]:
    print("second number is greatest")
    num = Var1[1]
else:
    print("third number is greatest")
    num = Var1[2]
if num % 2 == 0:
    if num % 3 == 0:
        print(num)
    else:
        print(num)
else:
    if num % 3 == 0:
        print(num)
    else:
        print(num)