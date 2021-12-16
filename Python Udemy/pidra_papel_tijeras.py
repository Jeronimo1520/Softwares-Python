rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

decition=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
list=[rock,paper,scissors]

if decition >=3 or decition<0:
  print("type a valid number between 0 and 2")
  
else:
   print(list[decition])
   print("Computer chose: ")
   computer_dect=random.randint(0,2)

   if computer_dect==0:
    print(rock)
   elif computer_dect==1:
    print(paper)
   else:
    print(scissors)

   if computer_dect==decition:
    print("It's a draw")
   elif computer_dect == 0 and decition==1 or computer_dect==2 and decition==0 or computer_dect==1 and decition==2:
    print("You win")
   elif computer_dect==0 and decition==2 or computer_dect==1 and decition==0 or computer_dect==2 and decition==1:
    print("You lose")
   else:
    print("you lose")