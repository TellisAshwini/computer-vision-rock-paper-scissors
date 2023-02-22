import random

def get_computer_choice():
    choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice
    
def get_user_choice():
    user_choice = input("Please enter your choice here: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    #print(computer_choice, user_choice)
    if (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'scissors')  or (computer_choice == 'scissors' and user_choice == 'rock'):
        print("You won!")
    elif (computer_choice == 'paper'and user_choice == 'rock') or (computer_choice == 'scissors' and user_choice == 'paper')  or (computer_choice == 'rock' and user_choice == 'scissors'):
        print("You lost")
    elif (user_choice == 'rock' and computer_choice == 'rock') or (user_choice == 'paper' and computer_choice == 'paper')  or (user_choice == 'scissors' and computer_choice == 'scissors'):
        print("It is a tie!")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    return winner

play()