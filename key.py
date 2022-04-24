import pygame
import os

BLACK = ( 0, 0, 0)
GREEN = ( 12, 156, 9)

class Key:

    def __init__(self, note, soundfile_name, x, y, black, width, height):
        self.mNote = note
        self.mSoundFile = soundfile_name
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mBlack = black
        return

    def getNote(self):
        return self.mNote

    def getSoundFileName(self):
        return self.mSoundFile

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getHeight(self):
        return self.mHeight

    def getWidth(self):
        return self.mWidth

    def getBlack(self):
        return self.mBlack

    def setNote(self, note):
        self.mNote = note

    def setSoundFileName(self, soundFileName):
        self.mSoundFile = soundFileName

    def setX(self, x):
        self.mX = x

    def setY(self, y):
        self.mY = y

    def setHeight(self, height):
        self.mHeight = height

    def setWidth(self, width):
        self.mWidth = width

    def setBlack(self, black):
        self.mBlack = black

    def resetKey(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
    
    def draw(self, surface, col):
        points = [(self.mX, self.mY), (self.mX, (self.mY + self.mHeight)), ((self.mX + self.mWidth), (self.mY + self.mHeight)), ((self.mX + self.mWidth), self.mY)]
        if col == 0:
            if self.mBlack:
                pygame.draw.polygon(surface, BLACK, points, 0)
            else:
                pygame.draw.polygon(surface, BLACK, points, 1)
        if col == 1:
            if self.mBlack:
                pygame.draw.polygon(surface, GREEN, points, 0)
                pygame.draw.polygon(surface, BLACK, points, 1)
            else:
                pygame.draw.polygon(surface, GREEN, points, 0)
                pygame.draw.polygon(surface, BLACK, points, 1)

    def isClicked(self, pos):
        if (pos[0] >= self.mX and pos[0] <= self.mX + self.mWidth) and (pos[1] >= self.mY and pos[1] <= self.mY + self.mHeight):
            return True
        return False

    def playSound(self, channel):
        script_dir = os.path.dirname(__file__)
        sound_path = sound_path = "sounds" + os.path.sep + "keys" + os.path.sep + self.mSoundFile
        path = os.path.join(script_dir, sound_path)
        sound = pygame.mixer.Sound(path)
        channel.play(sound)
        #channel.stop()

