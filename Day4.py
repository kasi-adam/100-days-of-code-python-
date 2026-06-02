import random
print("Welcome to Rock Paper Scissors")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices=["rock","paper","scissors"]
computer =random.choice(choices)
users_choice=input("Which choice are you making?\n Rock, Paper or Scissors? ").lower().strip()
print("You chose\n")
if users_choice=="rock":
    print(rock)
elif users_choice=="paper":
    print(paper)
else:
    print(scissor)
print("computer chose:\n")
if computer=="rock":
    print(rock)
elif computer=="paper":
    print(paper)
else:
    print(scissor)
if users_choice==computer:
    print("It is a draw. Try again!")
elif ((users_choice=="rock" and computer=="paper") or
      (users_choice=="paper" and computer=="scissors") or
      (users_choice=="scissors" and computer=="rock")):
    print("Computer wins!")
else:
    print("Computer lost! you won! congratulations!\n"
          "Head over to www.python.org to claim your prize!")

