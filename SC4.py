#Name: Austin B.
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

import random

players = int(input("enter the number of players: "))
for ratings in range(players):
    model1 = int(input("enter a rating between 1 and 5: "))
    model1a = int(input("enter a rating between 1 and 5: "))
    model1b = int(input("enter a rating between 1 and 5: "))
    model1c = int(input("enter a rating between 1 and 5: "))
    while model1 >= 6:
        model1 = int(input("error, enter a rating between 1 and 5: "))
    advmd = 0
    advmd += model1 + model1a + model1b + model1c / players
    print(advmd)