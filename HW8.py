#Name:Austin B.
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library

#2. print "Hello World!"

#3. Create three different variables that each randomly generate an integer between 1 and 10

#4. Print the three variables from #3 on the same line.

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.

#6. Print each result from #5 on the same line.

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

#8. Sort the list in #7 and print it.

#9. Add together the highest three numbers in the list from #7 and print the result.

#10. Create a list with 5 names of other students in this class and print the list.

#11. Shuffle the list in #10 and print the list again.

#12. Print a random choice from the list of names from #10.

import random
print("Hello World")
Var1 = random.randint(1,10)
Var2 = random.randint(1,10)
Var3 = random.randint(1,10)
print(Var1, Var2, Var3)
Var4 = Var1 + 2
Var5 = Var2 - 4
Var6 = Var3 * 1.5
print(Var4, Var5, Var6)
Var7 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
Var7.sort(reverse=True)
print(Var7)
Var8 = Var7[0] + Var7[1] + Var7[2]
print(Var8)
Var9 = ["Santi", "Ethan", "Anthony", "Wyatt", "Jake"]
print(Var9)
random.shuffle(Var9)
print(Var9)
Var10 = random.choice(Var9)
print(Var10)