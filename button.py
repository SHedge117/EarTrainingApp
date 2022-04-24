import pygame
import text


class Button:

    def __init__(self, x, y, height, string, r, g, b):
        self.mX = x
        self.mY = y 
        #self.mWidth = width
        self.mHeight = height
        self.mText = text.Text(string, x, y+height, height)
        self.mWidth = self.mText.getTextWidth()
        self.mRed = r
        self.mBlue = b
        self.mGreen = g

    def draw(self, surface):
        points = [(self.mX, self.mY), (self.mX, (self.mY + self.mHeight)), ((self.mX + self.mWidth), (self.mY + self.mHeight)), ((self.mX + self.mWidth), self.mY)]
        pygame.draw.polygon(surface, (self.mRed, self.mGreen, self.mBlue), points, 0)
        self.mText.draw(surface)
    
    def resetButton(self, x, y, height):
        self.mX = x
        self.mY = y 
        self.mHeight = height
        self.mText.resetText(x, y+height, height)
        self.mWidth = self.mText.getTextWidth()

    def isClicked(self, pos):
        if (pos[0] >= self.mX and pos[0] <= self.mX + self.mWidth) and (pos[1] >= self.mY and pos[1] <= self.mY + self.mHeight):
            return True
        return False

    def hover(self):
        self.mText.changeWhite()
        return

    def notHover(self):
        self.mText.changeBlack()
        return

