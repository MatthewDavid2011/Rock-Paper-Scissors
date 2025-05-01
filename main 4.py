import random

Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper= '''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

Scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''



#Rock Paper Scissors
#The rules are: 
choices= [Rock,Paper,Scissors]
user_input = int(input("Pick 0 for rock 1 for paper or 2 for scissors"))
print(choices[user_input])
computer_choice = random.randint (0,2)
print("the computer choice is")
print(choices[computer_choice])
if user_input >2or user_input <0:

    print("You have entered a invalid number.")
elif user_input==0 and computer_choice==2 or user_input== 1 and computer_choice==0 or user_input==2 and computer_choice==1:
    print("you win!")
elif user_input==0 and computer_choice==0 or user_input==1 and computer_choice==1 or user_input==2 and computer_choice==2:
    print("it was a draw")
else:
    print("you lose")


