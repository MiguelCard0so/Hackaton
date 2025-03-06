import pygame
import numpy as np

class Menu:
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items
    
class Button:
    def __init__(self, window, text, pos, height, width, color, border, x, y):
        self.window = window
        self.text = text
        self.pos = pos
        self.height = height
        self.width = width
        self.color = color
        self.border = border
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height), self.border)
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render(self.text, 1, (0, 0, 0))
        self.window.blit(text, (self.x + self.width//2 - text.get_width()//2, self.y + self.height//2 - text.get_height()//2))

    
