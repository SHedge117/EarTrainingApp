import pygame

class ProgressBar:

    def __init__(self, x, y, width, height, sections):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height 
        self.mSections = sections
        self.mCurrentSection = 0

    def incrementSection(self):
        self.mCurrentSection += 1
        if(self.mCurrentSection > self.mSections):
            self.mCurrentSection = self.mSections
        return

    def draw(self, surface):
        # Fill in progress rect
        x_fac = self.mCurrentSection/self.mSections
        new_w = self.mWidth * x_fac
        prog_points = [(self.mX, self.mY), (self.mX, (self.mY + self.mHeight)), ((self.mX + new_w), (self.mY + self.mHeight)), ((self.mX + new_w), self.mY)]
        pygame.draw.polygon(surface, (0, 255, 0), prog_points, 0)

        # Draw Bar outline
        points = [(self.mX, self.mY), (self.mX, (self.mY + self.mHeight)), ((self.mX + self.mWidth), (self.mY + self.mHeight)), ((self.mX + self.mWidth), self.mY)]
        pygame.draw.polygon(surface, (0, 0, 0), points, 1)

    def resetBar(self, x, y, w, h):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
