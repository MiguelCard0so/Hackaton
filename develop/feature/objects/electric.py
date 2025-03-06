import pygame
import numpy as np

class Lever:
    def __init__(self):
        self.state = True

    def flip(self):
        self.state = not self.state


class Door:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

    def open(self):
        self.state = True

    def close(self):
        self.state = False

    def is_open(self):
        return self.state


class MovableObject:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

    def move(self, direction):
        