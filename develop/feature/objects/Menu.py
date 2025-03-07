import pygame
import numpy as np

class Menu:
    def __init__(self, items):
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)    
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)
        self.MENU = 0
        self.GAME = 1
        self.OPTIONS = 2
        self.current_state = self.MENU
        self.menu_options = items
        self.selected_option = 0
        self.menu_options = ["Start Game", "Options", "Exit"]


    
    def get_items(self):
        return self.items
    
    # Function to check collision and prevent overlapping
    def handle_collision(rect1, rect2):
        if rect1.colliderect(rect2):
            if rect1.x < rect2.x:
                rect1.right = rect2.left
            else:
                rect1.left = rect2.right
            if rect1.y < rect2.y:
                rect1.bottom = rect2.top
            else:
                rect1.top = rect2.bottom
    
    # Function to draw the menu
    def draw_menu(self):
        self.screen.fill(self.WHITE)
        title = font.render("Block Collision Game", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(self.menu_options):
            color = self.BLACK if i == self.selected_option else self.GRAY
            text = self.small_font.render(option, True, color)
            self.screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, 250 + i * 70))

    
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

    
