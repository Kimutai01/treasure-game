print("___________________________________  
| _____ |   | ___ | ___ ___ | |   | |
| |   | |_| |__ | |_| __|____ | | | |
| | | |_________|__ |______ |___|_| |
| |_|   | _______ |______ |   | ____|
| ___ | |____ | |______ | |_| |____ |
|___|_|____ | |   ___ | |________ | |
|   ________| | |__ | |______ | | | |
| | | ________| | __|____ | | | __| |
|_| |__ |   | __|__ | ____| | |_| __|
|   ____| | |____ | |__ |   |__ |__ |
| |_______|_______|___|___|___|_____|
")
print("Welcome to the treasure island \nYour mission is to find the treasure")
crossroad = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
cross_road = crossroad.lower()

if cross_road == "right":
    print("There are lions. game over")
else:
    river = input("There's a river. Do you want to swim or wait? Type 'swim' or wait)
    river_choice = river.lower()
    if river_choice == 'swim':
        print("Game Over! the river is full of crocodiles")
    else:
        door = input("You have arrived at a room. There are three doors red,blue and yellow type red, blue or red")
        door_choice = door.lower()
        if door_choice == 'red':
            print("there's fire in the room! Game Over")
        elif door_choice == 'blue':
            print("there's a snake. Game over")
        else:
            print("You have found the treasure you have won!!")
