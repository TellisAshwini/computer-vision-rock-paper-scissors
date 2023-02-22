import random

def get_computer_choice():
    choice_list = ["Rock", "Paper", "Scissors"]
    return computer_choice = random.choice(choice_list)
    

def get_user_choice():
    user_choice = input("Please enter your choice here: ")
    return user_choice