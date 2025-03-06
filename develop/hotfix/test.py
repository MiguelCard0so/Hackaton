import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Collision Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Game states
MENU = 0
GAME = 1
OPTIONS = 2
current_state = MENU

# Menu options
menu_options = ["Start Game", "Options", "Exit"]
selected_option = 0

# Player classes
class Player:
    def __init__(self, speed, pos, range):
        self.killed = False
        self.speed = speed  # Speed in pixels per second
        self.pos = pos  # Position as a pygame.Rect
        self.color = None
        self.range = range

    def move(self, keys, dt, controls):
        normal_move = self.speed * dt

        if keys[controls["up"]]:
            self.pos.y -= normal_move
        if keys[controls["down"]]:
            self.pos.y += normal_move
        if keys[controls["left"]]:
            self.pos.x -= normal_move
        if keys[controls["right"]]:
            self.pos.x += normal_move
        if keys[controls["up"]] and keys[pygame.K_LSHIFT]:
            self.pos.y -= 2 * normal_move
        if keys[controls["down"]] and keys[pygame.K_LSHIFT]:
            self.pos.y += 2 * normal_move
        if keys[controls["left"]] and keys[pygame.K_LSHIFT]:
            self.pos.x -= 2 * normal_move
        if keys[controls["right"]] and keys[pygame.K_LSHIFT]:
            self.pos.x += 2 * normal_move

    def scream(self):
        return self.scream, self.color

class Twin1(Player):
    def __init__(self, speed, pos, range):
        super().__init__(speed, pos, range)
        self.color = (0, 255, 0)  # Green

class Twin2(Player):
    def __init__(self, speed, pos, range):
        super().__init__(speed, pos, range)
        self.color = (128, 0, 128)  # Purple

# Create players
player1 = Twin1(speed=300, pos=pygame.Rect(100, 100, 50, 50), range=100)
player2 = Twin2(speed=300, pos=pygame.Rect(400, 300, 50, 50), range=100)

# Control schemes
controls_player1 = {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
}

controls_player2 = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
}

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
def draw_menu():
    screen.fill(WHITE)
    title = font.render("Block Collision Game", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    for i, option in enumerate(menu_options):
        color = BLACK if i == selected_option else GRAY
        text = small_font.render(option, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 250 + i * 70))

# Function to draw the game
def draw_game():
    screen.fill(WHITE)
    pygame.draw.rect(screen, player1.color, player1.pos)
    pygame.draw.rect(screen, player2.color, player2.pos)

# Function to draw the options screen
def draw_options():
    screen.fill(WHITE)
    title = font.render("Options", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    text = small_font.render("This is the options screen.", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 300))

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle menu navigation
        if current_state == MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        current_state = GAME
                    elif selected_option == 1:  # Options
                        current_state = OPTIONS
                    elif selected_option == 2:  # Exit
                        running = False

        # Handle options screen
        elif current_state == OPTIONS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Go back to menu
                    current_state = MENU

    # Handle game controls
    if current_state == GAME:
        keys = pygame.key.get_pressed()
        player1.move(keys, dt, controls_player1)  # Twin1 uses WASD
        player2.move(keys, dt, controls_player2)  # Twin2 uses Arrow Keys

        # Handle collision
        handle_collision(player1.pos, player2.pos)

    # Draw the current screen based on the game state
    if current_state == MENU:
        draw_menu()
    elif current_state == GAME:
        draw_game()
    elif current_state == OPTIONS:
        draw_options()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()