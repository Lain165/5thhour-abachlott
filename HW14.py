#Name: Austin B.
#Class: 5th Hour
#Assignment: HW14
import random
import time
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

#5. Create a while loop that asks for a number input until the user inputs the number 0.

I = 5
while I >= 0:
    print(I)
    I -= 1
else:
    print("hello world")

J = 2
while J % 2 == 0:
    print(J)
    J += 2
    if J == 32:
        break

K = 1
while K <= 29:
    K += 1
    if K % 3 == 0:
        continue
    print(K)

L = random.randint(1, 6)
while L < 7:
    print(L)
    if L == 1:
        break
    L -= 1
M = (int(input("imput a number: ")))
while M < 7:
    print(M)
    if M > 0:
       M = (int(input("imput a lower number: ")))
    if M == 0:
        break