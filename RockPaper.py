import random
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

#Write your code below this line 👇

user = int(input("0 for Rock, 1 for Paper, 2 for Scissors "))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else :
    print(scissors)

comp = random.randint(0,2)
print(f"computer chose {comp} ")

if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
else :
    print(scissors)


if comp != user:
    if comp == 0 and user == 2:
        print("user wins")
    elif comp>user:
        print("comp wins")
    else:
        print("user wins")

elif comp == user:
    print("Draw")
else:
    print("Invalid")
    

