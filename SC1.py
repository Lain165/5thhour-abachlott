#Name: Austin B.
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

EnemyCreatures = {
    "Creature1" : {
    "Name": "Slime",
    "Health": 10,
    "Damage": 5,
    },
    "Creature2" : {
        "Name" : "Goblin",
        "Health" : 15,
        "Damage" : 10,
    },
    "Creature3" : {
        "Name" : "Bat",
        "Health" : 10,
        "Damage" : 15,
    },
    "Creature4" : {
        "Name" : "Ghoul",
        "Health" : 10,
        "Damage" : 20,
    },
    "CreatureBoss" : {
        "Name" : "Rock Golem",
        "Health" : 25,
        "Damage" : 25,
    },
    }
print(EnemyCreatures)
EnemyCreatures["Creature1"].update({"Damage" : 10})
EnemyCreatures["Creature2"].update({"Damage" : 15})
EnemyCreatures["Creature3"].update({"Damage" : 20})
EnemyCreatures["Creature4"].update({"Damage" : 25})
EnemyCreatures["CreatureBoss"].update({"Damage" : 30})
print(EnemyCreatures)

