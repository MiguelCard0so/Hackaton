import pygame
import numpy as np
from develop.feature.objects.player import Player



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.twin1 = Player(100, [self.width//2, self.height//2], 70)
        self.twin2 = Player(150, [self.width//4, self.height//4], 50)
        #self.bullets = []
        self.font = pygame.font.SysFont("comicsans", 50)
        self.score = 0

    

    def run(self):
        while self.running:
            self.clock.tick(30)
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.twin1.move(keys)
            self.twin2.move(keys)
        return None
    

if __name__ == "__main__":
    game = Game(800, 600)
    game.run()
    pygame.quit()
