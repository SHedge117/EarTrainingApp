import pygame
import config_var
import keyboard_screen
import time
import problem
import lesson
import menu_screen
import os

# FUTURE TODOS
# TODO: Make getting a note right or wrong more exciting
# TODO: Back Button from key screen that will return to menu in the middle of a lesson
# TODO: Sandbox mode where you can play whatever you want on the piano screen

LESSON_DICT = {} 

def readLessonFile(filename):
    fin = open(filename, 'r')
    lines = fin.readlines()
    lessoni = -1
    current_lesson_name = ""
    for line in lines:
        line.strip()
        parts = line.split()
        if parts[0] == "l":
            newLesson = lesson.Lesson(parts[1], [])
            current_lesson_name = parts[1]
            lessoni += 1
            LESSON_DICT[current_lesson_name] = newLesson
        if parts[0] == "p":
            notes = parts[2:]
            soundfile = parts[1]
            newProblem = problem.Problem(notes, soundfile)
            LESSON_DICT[current_lesson_name].addProblem(newProblem)

def main():
    pygame.init()

    # Open a new window
    size = (config_var.SCREEN_X, config_var.SCREEN_Y)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Ear Training App")


    carryOn = True
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    readLessonFile("lesson.txt")

    # State Variables

    # 0 for Menu screen, 1 for Keyboard screen
    MENU = 1

    # KEYBOARD VARIABLES
    PROBLEM_SOUND = True
    PAUSE = False
    KEYS_PRESSED = []
    STARTING_TIME = 0
    CURRENT_TIME = 0

    # MENU VARIABLES
    LESSON_SELECTED = False

    pygame.mixer.init(channels=2)

    m_screen = menu_screen.MenuScreen(screen)
    # -------- Main Program Loop -----------
    while carryOn:

        CURRENT_TIME = time.time()
        # Grab mouse position to see if it hovers over any buttons
        pos = pygame.mouse.get_pos()

        if(MENU == 1):
            # Start Button Hovers only when a lesson is selected
            m_screen.handleHover(pos, LESSON_SELECTED)

        if(MENU == 0):
            # Quit button will always hover, replay only when Pause is false
            key_screen.handleHover(pos, PAUSE)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we can exit the while loop

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if(MENU == 1):

                    # Sees if a lesson has been selected
                    if m_screen.handleLessonMouseEvents(pos):
                        # Only changes from False to True NEVER True to False
                        LESSON_SELECTED = True

                    # If the start button is clicked with a lesson selected, it will start the keyboard screen with the selected lesson
                    if m_screen.handleStartMouseEvents(pos) and LESSON_SELECTED == True:

                        # READ SELECTED LESSON FROM LESSON DICT
                        myLesson = LESSON_DICT[m_screen.mSelectedLessonText.getText()]

                        # CREATE KEYBOARD SCREEN
                        key_screen = keyboard_screen.KeyboardScreen(myLesson, screen)

                        # SET MENU TO 0
                        MENU = 0

                        # RESET MENU VARIABLES FOR WHEN LESSON IS DONE
                        LESSON_SELECTED = False

                if (MENU == 0):
                    # QUIT button will ALWAYS be active
                    key_screen.handleQuitMouseEvents(pos)
                
                    if PAUSE == False:
                        # Replays Sound if a problem sound is not already playing
                        key_screen.handleReplayMouseEvents(pos)

                        # Appends Key to KEYS_PRESSED and plays sound if there is no problem sound playing
                        key = key_screen.handleKeyMouseEvents(pos)
                        if key != "":
                            KEYS_PRESSED.append(key)

            if event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.size
                config_var.SCREEN_X = SCREEN_WIDTH
                config_var.SCREEN_Y = SCREEN_HEIGHT
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                if (MENU == 1):
                    m_screen.resetScreen(screen)
                if (MENU == 0):
                    key_screen.resetScreen(screen)
 
        
        # Menu Screen has no game logic, it is purely based on mouse events by the user

        # GAME LOGIC

        if MENU == 0:
        
            # if (STARTING_TIME != 0):
            #     print(CURRENT_TIME - STARTING_TIME)

            if (PAUSE == True and CURRENT_TIME - STARTING_TIME > 2):
                # PAUSE time is over, reset starting time and allow to play problem sound again
                PAUSE = False
                STARTING_TIME = 0
                PROBLEM_SOUND = True

                # If PAUSE is done and Lesson is done Transition back to menu
                if key_screen.mTitleText.getText() == "Done":
                
                    # RESET ALL Keyboard Variables
                    PROBLEM_SOUND = True
                    PAUSE = False
                    KEYS_PRESSED = []
                    STARTING_TIME = 0
                    CURRENT_TIME = 0

                    # Set Menu Flag
                    MENU = 1

                    # Resize Menu screen to current screen
                    m_screen.resetScreen(screen)

            if PAUSE == False and MENU == 0:   
                key_screen.handleUnPause()
                # KEYBOARD SCREEN GAME LOOP
                key_screen.playProblem(PROBLEM_SOUND)
                PROBLEM_SOUND = False

                # WAIT FOR USER TO PRESS TWO KEYS
                if len(KEYS_PRESSED) == 2:

                    # Send to Keyboard Screen to see if problem was correct and handle the aftermath
                    key_screen.handleCorrect(KEYS_PRESSED)

                    # Reset Keys Pressed
                    KEYS_PRESSED = []
                
                    # # Set Problem Sound to True to play new or old problem's sound
                    # PROBLEM_SOUND = True

                    STARTING_TIME = time.time()
                    PAUSE = True


            
        # --- Drawing code should go here 
        screen.fill(config_var.WHITE)

        if (MENU == 0):
            key_screen.draw()
        else:
            m_screen.draw()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
 
    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

if __name__ == "__main__":
    main()