import pygame
import sys
import random
import numpy as np
import time
from pygame.locals import *

running = True

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title
pygame.display.set_caption("Nome do Jogo")

# GAME LOOP
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



#if __name__ == "__main__":
#    print("Hello World")