import pygame
import numpy as np

class Player:
    def __init__(self, speed, pos, range):
        self.killed = False
        self.inventory = []
        self.speed = speed #300
        self.inventory = None
        self.pos = pos
        self.color = None
        self.range = range

    def move(self, keys):
        dt = 0
        normalMove = self.speed * dt

        if keys[pygame.K_w]:
            self.pos.y -= normalMove
        if keys[pygame.K_s]:
            self.pos.y += normalMove
        if keys[pygame.K_a]:
            self.pos.x -= normalMove
        if keys[pygame.K_d]:
            self.pos.x += normalMove
        if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
            self.pos.y -= 2 * normalMove
        if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
            self.pos.y += 2 * normalMove
        if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
            self.pos.x -= 2 * normalMove
        if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
            self.pos.x += 2 * normalMove

        
    
    def scream(self):
        return self.scream, self.color

class Twin1(Player):
    def __init__(self, speed, pos, range):
        super().__init__(speed, pos, range)
        super.inventory = []
        self.color = (0, 255, 0)
    
class Twin2(Player):
    def __init__(self, speed, pos, range):
        super().__init__(speed, pos, range)
        super.inventory = []
        self.color = (128, 0, 128)