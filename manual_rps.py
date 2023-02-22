import random

def get_computer_choice():
    choice_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice
    

def get_user_choice():
    user_choice = input("Please enter your choice here: ")
    return user_choice

computer_choice = get_computer_choice()
user_choice = get_user_choice()

def get_winner(computer_choice, user_choice ):
    print(computer_choice, user_choice)
    if (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Scissors')  or (computer_choice == 'Scissors' and user_choice == 'Rock'):
        print("You won")
    elif (user_choice == 'Rock' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Scissors')  or (user_choice == 'Scissors' and computer_choice == 'Rock'):
        print("You lost")
    elif (user_choice == 'Rock' and computer_choice == 'Rock') or (user_choice == 'Paper' and computer_choice == 'Paper')  or (user_choice == 'Scissors' and computer_choice == 'Scissors'):
        print("It is a tie!")

get_winner(computer_choice, user_choice)