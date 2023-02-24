import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    countdown = 3
    start_time = time.time()
    while (time.time()-start_time < countdown): 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction

def get_winner(computer_choice, user_choice):
    #print(computer_choice, user_choice)
    if (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'scissors')  or (computer_choice == 'scissors' and user_choice == 'rock'):
        print("You won!")
        return 0
    elif (computer_choice == 'paper'and user_choice == 'rock') or (computer_choice == 'scissors' and user_choice == 'paper')  or (computer_choice == 'rock' and user_choice == 'scissors'):
        print("You lost")
        return 1
    elif (user_choice == 'rock' and computer_choice == 'rock') or (user_choice == 'paper' and computer_choice == 'paper')  or (user_choice == 'scissors' and computer_choice == 'scissors'):
        print("It is a tie!")

def play():
    computer_wins = 0
    user_wins = 0
    rounds_played = 0
    while rounds_played < 5:
        computer_choice = get_computer_choice()
        user_choice_prediction = get_prediction()  
        user_choice_list = []
        for choice in user_choice_prediction[0]:
            user_choice_list.append(choice)
        high_probability = user_choice_list.index(max(user_choice_list))
        user_choice_list[0] = 'rock'
        user_choice_list[1] = 'paper'
        user_choice_list[2] = 'scissors'
        user_choice_list[3] = 'nothing'
        user_choice = user_choice_list[high_probability]
        print(f'you chose {user_choice}')
        print(f'computer chose {computer_choice}')
        winner = get_winner(computer_choice, user_choice)
        if winner == 0:
            user_wins += 1
            rounds_played += 1
            if user_wins > computer_wins and user_wins == 3:
                print("Congratulations you have won the game")
        elif winner == 1:
            computer_wins += 1
            rounds_played += 1
            if user_wins < computer_wins and computer_wins == 3:
                print("Sorry you lost the game")

play()