import random

computer_choice = random.choice(['rock','paper','scissors'])

user_choice = input('Enter - rock,paper or scrissors')

if computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('win')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('win')
else:
    print('You lose')