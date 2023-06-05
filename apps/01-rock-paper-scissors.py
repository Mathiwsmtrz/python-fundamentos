import random

options = ('rock', 'paper', 'scissors')
win = False

while win == False:
    user_option = input('!!! Play rock paper or scissors => ').lower()
    computer_option = random.choice(options)
    win = True

    print('user is:', user_option)
    print('computer is:', computer_option)

    if not user_option in options:
        win = True
        print('Invalid option for user')
    elif user_option == computer_option:
        win = False
        print('dead heat')
    elif user_option == 'rock' and computer_option == 'paper':
        print('computer win')
    elif user_option == 'paper' and computer_option == 'rock':
        print('user win')
    elif user_option == 'paper' and computer_option == 'scissors':
        print('computer win')
    elif user_option == 'scissors' and computer_option == 'paper':
        print('user win')
    elif user_option == 'scissors' and computer_option == 'rock':
        print('computer win')
    elif user_option == 'rock' and computer_option == 'scissors':
        print('user win')
