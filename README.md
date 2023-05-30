# Computer Vision RPS

Rock-Paper-Scissors is a hand game usually played between two people, in which each player simultaneously forms one of the three shapes with an outstretched hand rock, paper and scissor. 

A closed fist signifies a `rock` (✊). A flat hand signifies a `paper` (✋) and a fist with the index finger and middle finger extended, forming a V signifies `scissor` (✌).
 
The game goes by this logic, the paper covers rock, scissors cuts paper and rock crushes scissors. Hence paper beats rock, scissors beat paper and rock beats scissors. 

The user, starts by saying aloud “Rock! Paper! Scissors!” and then make one of these 3 shapes in hand simultaneously. Using the above logic the winner is decided.

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/1_aicore_rps.png" width = "550" height = "240" />

Rock-Paper-Scissors project is a part of my training at AiCore. This project is build using computer vision where the user makes the hand gesture when the camera is on, and the computer randomly chooses between the `rock`, `paper` or `scissors` and these are compared to check if user wins or loses.  This game is played in 5 rounds and the user wins the game if the user wins at least in 3 rounds.
> ## Milestone 1:

Git is a distributed version control system that manages multiple versions of source code and record them into a repository. GitHub is the cloud-based platform used in this project. It serves as a location for uploading copies of a Git repository for collaboration.

`computer-vision-rock-paper-scissors` is a repository created in the GitHub. 

The bash terminal in the VSCode is a platform used to run all the commands for Git and for running the python script.
Below are some basic commands that we frequently use in the bash terminal.
- ```git clone``` command clones the `computer-vision-rock-paper-scissors` repository in the GitHub to the bash terminal in the local machine
- ```git add``` and ```git commit``` commands are frequently used to stage changes and commit them to the repository in the local machine.
- ```git push``` command is used to push the committed changes in the  local repository to the GitHub repository.

> ## Milestone 2:

Teachable Machine (TM) is an AI experiment by Google. It is a web-based tool that makes it fast and easy to create machine learning models without any expertise or coding accessible to everyone.

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/2_teachable_machine.png" width = "550" height = "290" />

Using the image project, four classes are created `rock`, `paper`, `scissor` and `nothing`. Each class is trained with images of me, showing each option to the webcam or by uploading the images. The `Nothing` class represents the lack of option in the image. The more images you train with, the more accurate the model will be.

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/3_classes_teachable_machine_image.png" width = "550" height = "290" />


Once the model is trained with the images, the model can be tested making one of the hand gestures and the output will be in terms of probability of the gesture being one those classes we created. Here we can see the output as `scissors` with 98% accuracy

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/4_tm_scissors.png" width = "130" height = "200" />

 This model is then downloaded, and the files are saved as `keras_model.h5` and `labels.txt` in the repository.

> ## Milestone 3:
 The required libraries for this project are installed `opencv-python`, `tensorflow`, and `ipykernel`.

 OpenCV is library lets you create a video capture object that is helpful to capture videos through webcam and then you may perform desired operations on that video. Tensorflow library helps to load the keras model `keras_model.h5`  and the IPython kernel is the Python execution backend for Jupyter.

 > ## Milestone 4:

 To understand the working of the game better we first code this game by user manually entering "rock", "paper" or "scissors" using the `input` function and then later replacing the manual input with the computer vision. 
 
 The below function `get_user_choice` asks for user input and stores it in `user_choice` variable.

```
def get_user_choice():
    user_choice = input("Please enter your choice here: ")
    return user_choice
```

The machine randomly chooses between the "rock", "paper" and "scissors" from the `choice_list`. This is performed by importing the random module as shown below and stores it in `computer_choice` variable.

```
def get_computer_choice():
    choice_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice
```

`get_winner` function takes in `computer_choice` and `user_choice` as its parameters and decides if the user wins or loses by comparing these variables with the above logic of the game, using `if statemants` and prints a message saying 'You lose' or 'You win' or 'It's a tie' based on the conditions. The `play` function calls the `get_winner` function to start the game.

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/5_manual_output.png" width = "250" height = "60" />

 > ## Milestone 5:

 Now the manual user input is replaced by computer vision by replacing the `user_choice` function by `get_prediction` function which loads the model and captures the gestures that user makes in front of the webcam and predicts the gesture using this model.

 The output of the model is in this format.
 [[0.00157476 0.0888878  0.8342281  0.07530936]]

 Here the probabilies of the hand gesture is shown. The first element signifies `rock`, second element signifies `paper`, third element signifies `scissors` and fourth element signifies `nothing`. The order is based on the classes created before training the model.

 In the above example we can see that the probability of the hand gesture to be scissors is 83% which is the highest, hence we consider scissors as its the highest probability.

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/7_chose_rock.png" width = "220" height = "160" />


The below script is used to load the model and capture the data in a array format which is of 1 frame and of 224 x 224 pixels with 3 channels RGB(Red, Green and Blue).

```
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
```

In a `while loop` the frame is created using `cap.read` function and the image(`data`) is captured. It keeps capturing the guestures and predicts the gesture using `model.predict`. `cv2.imshow` shows the frame in which the image is captured. This loop continues until user presses 'c' in the keyboard.

```
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data, verbose = 0)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
```
While playing the game we have been saying aloud “Rock! Paper! Scissors!”. Hence to do this we give a countdown as "3", "2", "1", "Go!" at that point the user shows the hand gesture. This is done using `time.time()` function.

The game should be repeated until either the computer or the user wins three rounds. The two variables `computer_wins` and `user_wins` which initialised to 0 and `computer_wins` is incremented by 1 when user loses and `user_wins` is incremented by 1 when user wins in the `play` function.

 The game is repeated using `while loop` until the `computer_wins` or the `user_wins` is equal to 3. 

 <img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/6_won_game_console.png" width = "300" height = "160" />

 If the `user_wins` is equal to 3 then a message is displayed saying, congratulations! and if the `computer_wins` is equal to 3 then a message is displayed saying, you lost the game.

 > ## Taking it even further

 To highlight the messages in the console while printing, I have imported `Fore` from `colorama` and imported 'art' to get fancy fonts.


 <img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/8_colorama.png" width = "280" height = "250" />

Text is added to the frame where the hand gestures are made for better understanding and to make it more user friendly. 

<img src = "https://raw.githubusercontent.com/TellisAshwini/computer-vision-rock-paper-scissors/main/Images/7_chose_rock.png" width = "220" height = "160" />

Throughout the project it was a great learning experience all together. This project can be a great start for those who would like to understand computer vision concept and have fun experiments with it and dig deeper.
  


















