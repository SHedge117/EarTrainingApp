import os
import pygame

# os.path directory separator

class Problem:

    def __init__(self, notes, soundfile):
        self.mNotes = notes
        self.mSoundFile = soundfile

    def playSound(self, channel):
        script_dir = os.path.dirname(__file__)
        sound_path = "sounds" + os.path.sep + "problems" + os.path.sep + self.mSoundFile
        path = os.path.join(script_dir, sound_path)
        sound = pygame.mixer.Sound(path)
        channel.play(sound)
        #channel.stop()

    def isCorrect(self, input):
        if self.mNotes == input:
            return True
        return False

    def getNotes(self):
        return self.mNotes

    def __eq__(self, other):
        if self.mNotes == other.mNotes:
            return True
        return False