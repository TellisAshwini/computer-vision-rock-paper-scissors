import random
import cv2 
from keras.models import load_model
import numpy as np 
import time 
from colorama import Fore
from art import *

class RPS:
    def __init__(self):
        self.choice_list = ["Rock", "Paper", "Scissors", "Nothing"]
        self.computer_choice = ''
        self.user_choice = ''

    def get_computer_choice(self):
        '''
        Attributes
        ---------- 
        choice_list       : list
            List of all possible choices of hand gesture.
        computer_choice   : str
            Random element chosen by the computer from the choice_list
        '''
        self.computer_choice = random.choice(self.choice_list[0:3])
        return self.computer_choice

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0) # #0 represents 'one' camera
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        countdown = 3
        start_time = time.time()
        while True: 
            ret, frame = cap.read()  # ret is boolean value capturing true or false, frame captures the array
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose = 0) #predicts the model 
            predicted_list = [prediction[0][0], prediction[0][1], prediction[0][2], prediction[0][3]]
            self.user_choice = self.choice_list[predicted_list.index(max(predicted_list))]
            mins, secs = divmod(round(3 - (time.time() - start_time)), 60) #gives a countdown as 3, 2, 1 
            timer = '{:2d}'.format(secs)
            if int(timer) > 3 or  int(timer) < 1 :
                timer = "Go!"
            #Adds text in the frame 
            image = cv2.putText(frame, 'You chose '+ self.user_choice, (150, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            image = cv2.putText(frame, 'Countdown: '+ timer, (180, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
            image = cv2.putText(frame, 'Press c to continue', (150, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA) 
            cv2.imshow('frame', image) # shows the frame to capture image with the name, 'frame'
            if cv2.waitKey(1) & 0xFF == ord('c'): # Press c to close the window
                break
        
        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
        return self.user_choice

    def get_winner(self):
        '''
        Attributes:
        -----------
        win     : bool
            Conditions for the user to win the round
        tie     : bool
            Condition for a tie

        Checks for the condition and decides who wins each round
            - If win is True then the user wins the round
            - If tie is True then its a tie and the round is again repeated
            - If the both the above conditions are false then conputer wins the game for that round
        '''
        self.get_prediction()
        self.get_computer_choice()
        print(f'user choice: {self.user_choice}, computer choice: {self.computer_choice}')
        win = (self.computer_choice == 'Rock' and self.user_choice == 'Paper') or (self.computer_choice == 'Paper' and self.user_choice == 'Scissors') or (self.computer_choice == 'Scissors' and self.user_choice == 'Rock')
        tie = (self.user_choice == 'Rock' and self.computer_choice == 'Rock') or (self.user_choice == 'Paper' and self.computer_choice == 'Paper') or (self.user_choice == 'Scissors' and self.computer_choice == 'Scissors')
    
        if (self.user_choice == 'Nothing'):
            print(Fore.CYAN + 'Nothing was chosen please try again' + Fore.RESET)
        elif tie:
            print(Fore.CYAN + "It is a tie!" + Fore.RESET)
        elif win:
            print(Fore.GREEN + "You won!" + Fore.RESET)
            return 'win'
        else:
            print(Fore.LIGHTRED_EX + "You lost" + Fore.RESET)
            return 'lose'

def play():
    '''
    Attributes:
    -----------
    game_result     : str
        Sets to 'lose' if computer wins, and sets to 'win' if user wins, in each round.
    computer_wins   : int
        Set to 0 initially and increments everytime the computer wins a round (game_result = 'lose')
    user_wins       : int
        Set to 0 initially and increments everytime the user wins a round (game_result = 'win')
    Game continues until one of the 2 variables increments to 3
        
    Checks for the condition and decides who wins the game  
        - If user_wins increments upto 3, then user wins the game
        - If computer increments upto 3, then computer wins the game
    '''
    game = RPS()
    computer_wins = 0 
    user_wins = 0
    print(Fore.LIGHTCYAN_EX + "Welcome to \n")
    tprint("Rock-Paper-Scissors","rand-small")
    print("You will win the game if you win 3 rounds")
    print("Lets play.. !!\n\n" + Fore.RESET)
    while user_wins <= 3 or computer_wins <= 3:
        game_result = game.get_winner()
        if game_result == 'win':
            user_wins += 1
        elif game_result == 'lose':
            computer_wins += 1
        if user_wins == 3 or computer_wins == 3:
            if user_wins > computer_wins:
                print(Fore.GREEN + "Congratulations you have won the game" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "Sorry you lost the game" + Fore.RESET)
            break
        print(f'user_wins: {user_wins}, computer_wins: {computer_wins}')


if __name__ == "__main__":
    play()