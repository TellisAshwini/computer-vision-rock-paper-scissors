import random

def get_computer_choice():
    choice_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice
    

def get_user_choice():
    user_choice = input("Please enter your choice here: ")
    return user_choice