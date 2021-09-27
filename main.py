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
        
