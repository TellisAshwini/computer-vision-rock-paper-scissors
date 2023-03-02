import random
import cv2 #creates a video capture object through webcam 
from keras.models import load_model #loads the model
import numpy as np 
import time 
from colorama import Fore #Adds colour to the print statements

class RPS:
    def __init__(self):
        self.choice_list = ["Rock", "Paper", "Scissors", "Nothing"]
        self.computer_choice = ''
        self.user_choice = ''

    def get_computer_choice(self):
        #Chooses random element from the list 
        self.computer_choice = random.choice(self.choice_list[0:3])
        return self.computer_choice

    def get_prediction(self):
        #predicts the output of the model
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        countdown = 3
        start_time = time.time()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose = 0)       
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
            cv2.imshow('frame', image)
            # Press c to close the window
            if cv2.waitKey(1) & 0xFF == ord('c'): 
                break
        
        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
        return self.user_choice

    def get_winner(self):
        self.get_prediction()
        self.get_computer_choice()
        print(f'user choice: {self.user_choice}, computer choice: {self.computer_choice}')
        win = (self.computer_choice == 'Rock' and self.user_choice == 'Paper') or (self.computer_choice == 'Paper' and self.user_choice == 'Scissors') or (self.computer_choice == 'Scissors' and self.user_choice == 'Rock')
        tie = (self.user_choice == 'Rock' and self.computer_choice == 'Rock') or (self.user_choice == 'Paper' and self.computer_choice == 'Paper') or (self.user_choice == 'Scissors' and self.computer_choice == 'Scissors')
    
        #checks foe each condition from user and computer
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
    #starts the game
    game = RPS()
    computer_wins = 0 
    user_wins = 0
    print(Fore.LIGHTCYAN_EX + "Welcome to the Rock-Paper-Scissors game\n")
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


play()