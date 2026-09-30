#Name:Austin B.
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.

#3. Print the keys of the dictionary from #2.

#4. Print the values of the dictionary from #2

#5. Print one of the three numbers from the list by itself

#6. Using the update function, add a fourth key to the dictionary and give it a value.

#7. Print the entire dictionary from #2 with the updated key and value.

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

#9. Print the names of all three classmates on the same line.

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.

print("Hello World")
dictionary1 = {
    "randomkey1" : "randomvalue1",
    "randomkey2" : "randomvalue2",
    "3intergerkey" : [100, 189, 276]
}
print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1["3intergerkey"][1])
dictionary1.update({"randomkey3" : "randomvalue3"})
print(dictionary1)
studentdictionary = {
    "sd1" : {
    "Name" : "Jake",
    "Grade" : "10th grade",
    "5th hour" : "computer science",
    },
    "sd2" : {
    "Name" : "Ethan",
    "Grade" : "10th grade",
    "5th hour" : "computer science",
    },
    "sd3" : {
    "Name" : "Anthony",
    "Grade" : "9th grade",
    "5th hour" : "computer science",
    },
}
print(studentdictionary["sd1"]["Name"]), print(studentdictionary["sd2"]["Name"]), print(studentdictionary["sd3"]["Name"])
studentdictionary.pop("sd1")
print(studentdictionary)