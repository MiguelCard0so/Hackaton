import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
speedmod = 0

background = pygame.image.load("release/resources/Background.png")

# Define tile size
TILE_SIZE = 64

# Create a grid of tiles
GRID_WIDTH = screen.get_width() // TILE_SIZE
GRID_HEIGHT = screen.get_height() // TILE_SIZE

# Position control
player_pos = pygame.Vector2(GRID_WIDTH // 2, GRID_HEIGHT // 2)
player2_pos = pygame.Vector2(GRID_WIDTH // 2, GRID_HEIGHT // 2)

# Load the sprite image
player_image = pygame.image.load("D:/Downloads/Universidade/cenas de fora/hackathon/Hackaton/sprites/char.png").convert_alpha()
player2_image = pygame.image.load("D:/Downloads/Universidade/cenas de fora/hackathon/Hackaton/sprites/Green_Fuckwith.png").convert_alpha()

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw the sprite image at the player's tile position
    screen.blit(player_image, (player_pos.x * TILE_SIZE, player_pos.y * TILE_SIZE))
    screen.blit(player2_image, (player2_pos.x * TILE_SIZE, player2_pos.y * TILE_SIZE))
    screen.blit(background, (0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1
    if keys[pygame.K_s]:
        player_pos.y += 1
    if keys[pygame.K_a]:
        player_pos.x -= 1
    if keys[pygame.K_d]:
        player_pos.x += 1
    if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
        player_pos.y -= 2
    if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
        player_pos.y += 2
    if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        player_pos.x -= 2
    if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
        player_pos.x += 2

    if keys[pygame.K_UP]:
        player2_pos.y -= 1
    if keys[pygame.K_DOWN]:
        player2_pos.y += 1
    if keys[pygame.K_LEFT]:
        player2_pos.x -= 1
    if keys[pygame.K_RIGHT]:
        player2_pos.x += 1
    if keys[pygame.K_UP] and keys[pygame.K_RSHIFT]:
        player2_pos.y -= 2
    if keys[pygame.K_DOWN] and keys[pygame.K_RSHIFT]:
        player2_pos.y += 2
    if keys[pygame.K_LEFT] and keys[pygame.K_RSHIFT]:
        player2_pos.x -= 2
    if keys[pygame.K_RIGHT] and keys[pygame.K_RSHIFT]:
        player2_pos.x += 2

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()