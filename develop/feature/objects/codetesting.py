import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
speedmod = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(20, 700)

# Load the sprite image
player_image = pygame.image.load("C:/Users/migue/Documentos/GitHub/hackaton/Hackaton").convert_alpha()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw the sprite image
    screen.blit(player_image, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
        player_pos.x += 600 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
