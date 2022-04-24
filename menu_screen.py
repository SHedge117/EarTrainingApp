from distutils.command.config import config
import text
import config_var
import button

class MenuScreen:

    def __init__(self, surface):

        self.mTitleText1 = text.Text("Shawn's", (config_var.SCREEN_X * .5), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05))
        self.mTitleText2 = text.Text("Ear Training App", (config_var.SCREEN_X * .43), (config_var.SCREEN_Y * .13), (config_var.SCREEN_Y * .05))
        self.mIntervalText = text.Text("Intervals:", (config_var.SCREEN_X * .1), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mLessonSelected = False
        
        # INTERVAL BUTTONS

        self.mSecondsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .34), (config_var.SCREEN_Y * .05), "Seconds",  9, 127, 181)
        self.mThirdsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .42), (config_var.SCREEN_Y * .05), "Thirds", 9, 127, 181)
        self.mFourthsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .5), (config_var.SCREEN_Y * .05), "Fourths", 9, 127, 181)
        self.mFifthsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .58), (config_var.SCREEN_Y * .05), "Fifths", 9, 127, 181)
        self.mSixthsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .66), (config_var.SCREEN_Y * .05), "Sixths", 9, 127, 181)
        self.mSeventhsButton = button.Button((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .74), (config_var.SCREEN_Y * .05), "Sevenths", 9, 127, 181)

        self.mChordProgressionText = text.Text("Chord Progressions:", (config_var.SCREEN_X * .4), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mChordsComingSoonText = text.Text("COMING SOON!", (config_var.SCREEN_X * .4), (config_var.SCREEN_Y * .39), (config_var.SCREEN_Y * .05))

        self.mScaleText = text.Text("Scales:", (config_var.SCREEN_X * .79), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mScaleComingSoonText = text.Text("COMING SOON!", (config_var.SCREEN_X * .75), (config_var.SCREEN_Y * .39), (config_var.SCREEN_Y * .05))

        self.mSelectedText = text.Text("Selected Lesson:", (config_var.SCREEN_X * .3), (config_var.SCREEN_Y * .9), (config_var.SCREEN_Y * .05))
        self.mSelectedLessonText = text.Text("N/A", (config_var.SCREEN_X * .57), (config_var.SCREEN_Y * .9), (config_var.SCREEN_Y * .05))

        self.mStartButton = button.Button((config_var.SCREEN_X * .45), (config_var.SCREEN_Y * .92), (config_var.SCREEN_Y * .07), "START", 9, 127, 181)
        self.mSurface = surface



    def draw(self):
        self.mTitleText1.draw(self.mSurface)
        self.mTitleText2.draw(self.mSurface)
        self.mIntervalText.draw(self.mSurface)
        self.mChordProgressionText.draw(self.mSurface)
        self.mChordsComingSoonText.draw(self.mSurface)
        self.mScaleText.draw(self.mSurface)
        self.mScaleComingSoonText.draw(self.mSurface)
        self.mSecondsButton.draw(self.mSurface)
        self.mThirdsButton.draw(self.mSurface)
        self.mFourthsButton.draw(self.mSurface)
        self.mFifthsButton.draw(self.mSurface)
        self.mSixthsButton.draw(self.mSurface)
        self.mSeventhsButton.draw(self.mSurface)
        self.mSelectedText.draw(self.mSurface)
        self.mSelectedLessonText.draw(self.mSurface)

        self.mStartButton.draw(self.mSurface)

    def resetScreen(self, surface):
        self.mSurface = surface
        self.mTitleText1.resetText((config_var.SCREEN_X * .5), (config_var.SCREEN_Y * .08), (config_var.SCREEN_Y * .05))
        self.mTitleText2.resetText((config_var.SCREEN_X * .43), (config_var.SCREEN_Y * .13), (config_var.SCREEN_Y * .05))
        self.mIntervalText.resetText((config_var.SCREEN_X * .1), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mChordProgressionText.resetText((config_var.SCREEN_X * .4), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mChordsComingSoonText.resetText((config_var.SCREEN_X * .4), (config_var.SCREEN_Y * .39), (config_var.SCREEN_Y * .05))
        self.mScaleText.resetText((config_var.SCREEN_X * .79), (config_var.SCREEN_Y * .3), (config_var.SCREEN_Y * .05))
        self.mScaleComingSoonText.resetText((config_var.SCREEN_X * .75), (config_var.SCREEN_Y * .39), (config_var.SCREEN_Y * .05))
        self.mSecondsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .34), (config_var.SCREEN_Y * .05))
        self.mThirdsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .42), (config_var.SCREEN_Y * .05))
        self.mFourthsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .5), (config_var.SCREEN_Y * .05))
        self.mFifthsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .58), (config_var.SCREEN_Y * .05))
        self.mSixthsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .66), (config_var.SCREEN_Y * .05))
        self.mSeventhsButton.resetButton((config_var.SCREEN_X * .12), (config_var.SCREEN_Y * .74), (config_var.SCREEN_Y * .05))

        self.mSelectedText.resetText((config_var.SCREEN_X * .3), (config_var.SCREEN_Y * .9), (config_var.SCREEN_Y * .05))
        self.mSelectedLessonText.resetText((config_var.SCREEN_X * .57), (config_var.SCREEN_Y * .9), (config_var.SCREEN_Y * .05))

        self.mStartButton.resetButton((config_var.SCREEN_X * .45), (config_var.SCREEN_Y * .92), (config_var.SCREEN_Y * .07))

    def handleLessonMouseEvents(self, pos):
        if self.mSecondsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Seconds")
            return True

        if self.mThirdsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Thirds")
            return True

        if self.mFourthsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Fourths")
            return True

        if self.mFifthsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Fifths")
            return True

        if self.mSixthsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Sixths")
            return True

        if self.mSeventhsButton.isClicked(pos):
            self.mSelectedLessonText.setString("Sevenths")
            return True


    def handleStartMouseEvents(self, pos):
        if self.mStartButton.isClicked(pos):
            return True
        return False
            
    def handleHover(self, pos, lesson_selected):
        if self.mSecondsButton.isClicked(pos):
            self.mSecondsButton.hover()
        else:
            self.mSecondsButton.notHover()

        if self.mThirdsButton.isClicked(pos):
            self.mThirdsButton.hover()
        else:
            self.mThirdsButton.notHover()

        if self.mFourthsButton.isClicked(pos):
            self.mFourthsButton.hover()
        else:
            self.mFourthsButton.notHover()

        if self.mFifthsButton.isClicked(pos):
            self.mFifthsButton.hover()
        else:
            self.mFifthsButton.notHover()

        if self.mSixthsButton.isClicked(pos):
            self.mSixthsButton.hover()
        else:
            self.mSixthsButton.notHover()

        if self.mSeventhsButton.isClicked(pos):
            self.mSeventhsButton.hover()
        else:
            self.mSeventhsButton.notHover()

        if self.mStartButton.isClicked(pos) and lesson_selected == True:
            self.mStartButton.hover()
        else:
            self.mStartButton.notHover()