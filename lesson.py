import os
import pygame

class Lesson:

    def __init__(self, lesson_name, problems):
        self.mLessonName = lesson_name
        self.mProblems = problems

    def getProblem(self, i):
        if i < len(self.mProblems):
            return self.mProblems[i]
        else:
            return -1

    def addProblem(self, problem):
        for i in range(len(self.mProblems)):
            if self.mProblems[i] == problem:
                return
        self.mProblems.append(problem)
        return

    def getLessonName(self):
        return self.mLessonName

    def getNumProblems(self):
        return len(self.mProblems)