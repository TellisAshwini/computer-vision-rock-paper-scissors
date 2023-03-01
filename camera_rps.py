import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RPS:
    def __init__(self, rounds_played = 0):
        self.choice_list = ["Rock", "Paper", "Scissors"]
        self.computer_choice = ''
        self.user_choice = ''
        self.rounds_played = rounds_played

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.choice_list)
        return self.computer_choice

    def get_prediction(self):
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
            mins, secs = divmod(round(3 - (time.time() - start_time)), 60)
            timer = '{:2d}'.format(secs)
            if int(timer) > 3:
                timer = '0'
            img = cv2.putText(frame, 'You chose '+ self.user_choice, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            img = cv2.putText(frame, 'Countdown: '+ timer, (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA) #yellow
            img = cv2.putText(frame, 'Press c to continue', (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA) #purple
            
            cv2.imshow('frame', img)
            
            if cv2.waitKey(1) & 0xFF == ord('c'): # Press q to close the window
                break

        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
        return self.user_choice

    def get_winner(self):
        self.get_prediction()
        self.get_computer_choice()
        print(f'user choice: {self.user_choice}, computer choice: {self.computer_choice}, rounds: {self.rounds_played}')
        win = (self.computer_choice == 'Rock' and self.user_choice == 'Paper') or (self.computer_choice == 'Paper' and self.user_choice == 'Scissors') or (self.computer_choice == 'Scissors' and self.user_choice == 'Rock')
        tie = (self.user_choice == 'Rock' and self.computer_choice == 'Rock') or (self.user_choice == 'Paper' and self.computer_choice == 'Paper') or (self.user_choice == 'Scissors' and self.computer_choice == 'Scissors')

        if (self.user_choice == 'nothing'):
            print('Nothing was chosen please try again')
        else:
            if tie:
                print("It is a tie!")
            elif win:
                print("You won!")
                self.rounds_played += 1
                return 'win'
            else:
                print("You lost")
                self.rounds_played += 1
                return 'lose'

def play():
    game = RPS()
    computer_wins = 0
    user_wins = 0
    while game.rounds_played < 5:
        game_result = game.get_winner()
        if game_result == 'win':
            user_wins += 1
        elif game_result == 'lose':
            computer_wins += 1
        if user_wins == 3 or computer_wins == 3:
            if user_wins > computer_wins:
                print("Congratulations you have won the game")
            else:
                print("Sorry you lost the game")
            break
        print(f'user_wins: {user_wins}, computer_wins: {computer_wins}, round: {game.rounds_played}')


play()