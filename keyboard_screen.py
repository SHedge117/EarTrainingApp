import pygame
import config_var
import key
import button
import text
import lesson
import problem
import time
import progress_bar
import os

class KeyboardScreen:

    def __init__(self, lesson, surface):
        self.mLesson = lesson
        self.mSurface = surface
        self.mTitleText = text.Text(self.mLesson.getLessonName(), (config_var.SCREEN_X * .5), (config_var.SCREEN_Y * .05), (config_var.SCREEN_Y * .05))
        self.mCurrentProblem = self.mLesson.getProblem(0)
        self.mProblemNum = 0

        self.mProblemChannel = pygame.mixer.Channel(0)
        self.mKeyChannel = pygame.mixer.Channel(1)

        self.mBlackKeys = []
        # BLACK KEYS
        cSharp1Key = key.Key("CSharp1", "cSharp1_key.wav",  ((config_var.SCREEN_X * .1) + (config_var.SCREEN_X * .05)),  (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys.append(cSharp1Key)
        dSharp1Key = key.Key("DSharp1", "dSharp1_key.wav", ((config_var.SCREEN_X * .1) + ((2 * (config_var.SCREEN_X * .089)) - (config_var.SCREEN_X * .016))), (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48))
        self.mBlackKeys.append(dSharp1Key)
        fSharpKey = key.Key("FSharp1", "fSharp1_key.wav", ((config_var.SCREEN_X * .1) + 3 * (config_var.SCREEN_X * .089) + (config_var.SCREEN_X * .05)), (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys.append(fSharpKey)
        gSharpKey = key.Key("GSharp1", "gSharp1_key.wav", ((config_var.SCREEN_X * .1) + 5 * (config_var.SCREEN_X * .089) - (config_var.SCREEN_X * .0275)), (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys.append(gSharpKey)
        aSharpKey = key.Key("ASharp1", "aSharp1_key.wav", ((config_var.SCREEN_X * .1) + 6 * (config_var.SCREEN_X * .089) - (config_var.SCREEN_X * .016)), (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys.append(aSharpKey)
        cSharp2Key = key.Key("CSharp2", "cSharp2_key.wav",  ((config_var.SCREEN_X * .1) + 7 * (config_var.SCREEN_X * .089) + (config_var.SCREEN_X * .05)),  (config_var.SCREEN_Y * .15), True, (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys.append(cSharp2Key)

        self.mWhiteKeys = []
        # WHITE KEYS
        c1Key = key.Key("C1", "c1_key.wav", (config_var.SCREEN_X * .1), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089) ,(config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(c1Key)
        d1Key = key.Key("D1", "d1_key.wav", ((config_var.SCREEN_X * .1) + (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089) , (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(d1Key)
        eKey = key.Key("E1", "e1_key.wav", ((config_var.SCREEN_X * .1) + 2 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(eKey)
        fKey = key.Key("F1", "f1_key.wav", ((config_var.SCREEN_X * .1) + 3 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089),(config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(fKey)
        gKey = key.Key("G1", "g1_key.wav", ((config_var.SCREEN_X * .1) + 4 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(gKey)
        aKey = key.Key("A1", "a1_key.wav", ((config_var.SCREEN_X * .1) + 5 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(aKey)
        bKey = key.Key("B1", "b1_key.wav", ((config_var.SCREEN_X * .1) + 6 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(bKey)
        c2Key = key.Key("C2", "c2_key.wav", ((config_var.SCREEN_X * .1) + 7 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(c2Key)
        d2Key = key.Key("D2", "d2_key.wav", ((config_var.SCREEN_X * .1) + 8 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), False, (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys.append(d2Key)

        self.mQuitButton = button.Button((config_var.SCREEN_X * .25), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05), "Quit", 9, 127, 181)
        self.mReplayButton = button.Button((config_var.SCREEN_X * .75), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05), "Replay", 9, 127, 181)
        self.mProgressBar = progress_bar.ProgressBar((config_var.SCREEN_X * .47), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .29),(config_var.SCREEN_Y * .05), self.mLesson.getNumProblems())

    def resetKeys(self):
        # WHITE KEYS
        self.mWhiteKeys[0].resetKey((config_var.SCREEN_X * .1), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089) ,(config_var.SCREEN_Y * .75))
        self.mWhiteKeys[1].resetKey(((config_var.SCREEN_X * .1) + (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[2].resetKey(((config_var.SCREEN_X * .1) + 2 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[3].resetKey(((config_var.SCREEN_X * .1) + 3 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[4].resetKey(((config_var.SCREEN_X * .1) + 4 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[5].resetKey(((config_var.SCREEN_X * .1) + 5 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[6].resetKey(((config_var.SCREEN_X * .1) + 6 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[7].resetKey(((config_var.SCREEN_X * .1) + 7 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))
        self.mWhiteKeys[8].resetKey(((config_var.SCREEN_X * .1) + 8 * (config_var.SCREEN_X * .089)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .089), (config_var.SCREEN_Y * .75))

    # BLACK KEYS
        self.mBlackKeys[0].resetKey( ((config_var.SCREEN_X * .1) + (config_var.SCREEN_X * .05)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055),  (config_var.SCREEN_Y * .48) )
        self.mBlackKeys[1].resetKey( ((config_var.SCREEN_X * .1) + ((2 * (config_var.SCREEN_X * .089)) - (config_var.SCREEN_X * .016))), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055),  (config_var.SCREEN_Y * .48) )
        self.mBlackKeys[2].resetKey( ((config_var.SCREEN_X * .1) + 3 * (config_var.SCREEN_X * .089) + (config_var.SCREEN_X * .05)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys[3].resetKey( ((config_var.SCREEN_X * .1) + 5 * (config_var.SCREEN_X * .089) - (config_var.SCREEN_X * .0275)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48))
        self.mBlackKeys[4].resetKey( ((config_var.SCREEN_X * .1) + 6 * (config_var.SCREEN_X * .089) - (config_var.SCREEN_X * .016)), (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )
        self.mBlackKeys[5].resetKey(   ((config_var.SCREEN_X * .1) + 7 * (config_var.SCREEN_X * .089) + (config_var.SCREEN_X * .05)),  (config_var.SCREEN_Y * .15), (config_var.SCREEN_X * .055), (config_var.SCREEN_Y * .48) )

    
    def resetScreen(self, surface):
        self.mSurface = surface
        self.resetKeys()
        self.mProgressBar.resetBar((config_var.SCREEN_X * .47), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .29),(config_var.SCREEN_Y * .05))
        self.mQuitButton.resetButton((config_var.SCREEN_X * .25), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05))
        self.mReplayButton.resetButton((config_var.SCREEN_X * .75), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05))
        self.mTitleText.resetText((config_var.SCREEN_X * .5), (config_var.SCREEN_Y * .05), (config_var.SCREEN_Y * .05))

    def draw(self):
        for key in self.mWhiteKeys:
            if key.getNote() == self.mCurrentProblem.getNotes()[0]:
                key.draw(self.mSurface, 1)
            else:
                key.draw(self.mSurface, 0)

        for key in self.mBlackKeys:
            if key.getNote() == self.mCurrentProblem.getNotes()[0]:
                key.draw(self.mSurface, 1)
            else:
                key.draw(self.mSurface, 0)
    
        self.mQuitButton.draw(self.mSurface)
        self.mReplayButton.draw(self.mSurface)
        self.mTitleText.draw(self.mSurface)
        self.mProgressBar.draw(self.mSurface)

    def handleHover(self, pos, PAUSE):

        if self.mQuitButton.isClicked(pos):
            self.mQuitButton.hover()
        else:
            self.mQuitButton.notHover()

        if PAUSE == False and self.mReplayButton.isClicked(pos):
            self.mReplayButton.hover() 
        else:
            self.mReplayButton.notHover()

    def handleQuitMouseEvents(self, pos):
        if self.mQuitButton.isClicked(pos):
            quit()

    def handleReplayMouseEvents(self, pos):
        if self.mReplayButton.isClicked(pos):
            if self.mProblemChannel.get_busy() == False:
                self.mCurrentProblem.playSound(self.mProblemChannel)

    def handleKeyMouseEvents(self, pos):
        if self.mProblemChannel.get_busy() == False:
            blackClicked = False
            for key in self.mBlackKeys:
                if key.isClicked(pos):
                    blackClicked = True
                    print(key.getNote())
                    key.playSound(self.mKeyChannel)
                    # Return to user to add to KEYS_PRESSED
                    return key.getNote()
            if not blackClicked:
                for key in self.mWhiteKeys:
                    if key.isClicked(pos):
                        print(key.getNote())
                        key.playSound(self.mKeyChannel)
                        # Return to user to add to KEYS_PRESSED
                        return key.getNote()
        # Return empty string if no keys were clicked or Problem channel was busy
        return ""

    def playProblem(self, problem_sound):

        # Will play problem sound if problem_sound is True
        if problem_sound == True:
            self.mCurrentProblem.playSound(self.mProblemChannel)

    def handleCorrect(self, keys_pressed):
                correct = self.mCurrentProblem.isCorrect(keys_pressed)
                if correct:
                    self.mTitleText.setString("Good!")
                    self.mProgressBar.incrementSection()
                    if self.mProblemNum == self.mLesson.getNumProblems()-1:
                        self.mTitleText.setString("Done")
                        # Transition back to menu screen
                        return True
                    else:
                        self.mProblemNum += 1
                        self.mCurrentProblem = self.mLesson.getProblem(self.mProblemNum)
                        return True
                else:
                    self.mTitleText.setString("Try Again")
                    return False

    def handleUnPause(self):
        self.mTitleText.setString(self.mLesson.getLessonName())

        
