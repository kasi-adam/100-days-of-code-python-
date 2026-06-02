print("Welcome to Treasure Island!\nYour goal is to find the treasure\n")
answer = input("Are you ready?!")
print("Great, let us begin!")
direction=input("You are at a cross road, which direction would you want to walk in?\nLeft or right?")
if direction=="right":
    print("Game Over sucker! You lost!")
else:
    answer=input("You've made it to the next part! you've arrived at a river, will you Swim or wait?")
    if answer=="swim":
        print("Game over! choose wisely next time :)")
    else:
        choice=input("Which door would you like to choose?\n red or blue? or yellow? ")
        if choice=="red":
            print("Game Over! You lost!")
        elif choice=="blue":
            print("Game Over! You lost. you were so close! :(")
        else:
            print("Congratulations! You won! Head over to the the URL below to claim your prize!\n www.pythonwinners.com")



