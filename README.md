# EarTrainingApp
Shawn Hedgepeth's Senior Project at Dixie State University Spring 2022


## Project Information
This app allows Musicians and anyone else interested to practice Ear Training. Ear Training is the process of being able to recognize pitches, rhythms and other musical patterns by just listening. It is an important skill for musicians which is why they need an efficient and easy way to practice.

## Code Structure
All code is put in the main repository folder. You can run this project by running the main.py file. The sounds required for this project are all contained in the **sounds** folder. The sounds will be split between **key** sounds and **problem** sounds. The path structure is important and will need to be changed in the code if it is changed.

## Lesson File
**lesson.txt** is the file containing the info that is read to create the lesson dictionary. While there isn't a way to add new lessons to the file without issues, users can switch the order of problems or add/delete them. In **lesson.txt** add a new line between any lesson beginning with "p". Add the sound file name and the two keys the user needs to press to answer correctly. The keys are named in a specific way (C1, CSharp1, C2, etc.). If the file does not have the keys in this format the code won't be able to process the correct key. Last thing is to make sure your **.wav** file is located in the **/sounds/problems** directory because that is where the code will expect it.

# Happy Ear Training!
