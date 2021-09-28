print("___________________________________")  
print("| _____ |   | ___ | ___ ___ | |   | |")
print("| |   | |_| |__ | |_| __|____ | | | |")
print("| | | |_________|__ |______ |___|_| |")
print("| |_|   | _______ |______ |   | ____|")
print("| ___ | |____ | |______ | |_| |____ |")
print("|___|_|____ | |   ___ | |________ | |")
print("|   ________| | |__ | |______ | | | |")
print("| | | ________| | __|____ | | | __| |")
print("|_| |__ |   | __|__ | ____| | |_| __|")
print("|   ____| | |____ | |__ |   |__ |__ |")
print("| |_______|_______|___|___|___|_____|")
print("Welcome to the treasure island \nYour mission is to find the treasure: " )
crossroad = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' :")
cross_road = crossroad.lower()

if cross_road == "right":
    print("There are lions. game over")
else:
    river = input("There's a river. Do you want to swim or wait? Type 'swim' or wait :")
    river_choice = river.lower()
    if river_choice == 'swim':
        print("Game Over! the river is full of crocodiles")
    else:
        door = input("You have arrived at a room. There are three doors red,blue and yellow type red, blue or yellow :")
        door_choice = door.lower()
        if door_choice == 'red':
            print("there's fire in the room! Game Over")
        elif door_choice == 'blue':
            print("there's a snake. Game over")
        else:
            print("You have found the treasure you have won!!")
