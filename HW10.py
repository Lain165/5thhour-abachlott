#Name: Austin B.
#Class: 5th Hour
#Assignment: HW10


#1. Print "Hello World!"

#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.

#3. Print A, B, and C on the same line.

#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.

#5. Make an if statement that prints if variable B is between 3 and 7, or not.

#6. Make an if statement that prints if variable C is even or odd.

#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20

#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.

print("Hello World")
import random
VarA = random.randint(1,10)
VarB = random.randint(1,10)
VarC = random.randint(1,10)
print(VarA, VarB, VarC)
if VarA > 5:
    print("Greater")
elif VarA < 5:
    print("Less")
else:
    print("Equal")
if VarB > 3 and VarB < 7:
    print("Inbetween")
else:
    print("Not inbetween")
if VarC % 2 == 0:
    print("Even")
else:
    print("Odd")
VarD = 3 + random.randint(1,20)
print(VarD)
if VarD > VarA + VarB + VarC:
    print("Greater")
elif VarD < VarA + VarB + VarC:
    print("Less")
else:
    print("Equal")