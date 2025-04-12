import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars")

# Load player image
player_img = pygame.image.load("images/neilbg.png")
player_img = pygame.transform.scale(player_img, (100, 100))

# Load star image
star_img = pygame.image.load("images/star1.png")
star_img = pygame.transform.scale(star_img, (25, 25))

# Player settings
player_pos = [WIDTH // 2, HEIGHT - player_img.get_height() * 2]

# Star settings
star_pos = [random.randint(0, WIDTH - star_img.get_width()), 0]
star_list = [star_pos]

# Game settings                                          
game_over = False
score = 0
clock = pygame.time.Clock()
speed = 5

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_img.get_width()
            elif event.key == pygame.K_RIGHT:
                x += player_img.get_width()
            player_pos[0] = x

    window.fill((0, 0, 0))

    # Update star positions
    for idx, star in enumerate(star_list):
        if star[1] >= 0 and star[1] < HEIGHT:
            star[1] += speed
        else:
            star_list.pop(idx)
            score += 1
            star_list.append([random.randint(0, WIDTH - star_img.get_width()), 0])

    # Draw stars
    for star in star_list:
        window.blit(star_img, (star[0], star[1]))

    # Draw player
    window.blit(player_img, (player_pos[0], player_pos[1]))

    # Collision detection
    for star in star_list:
        if star[1] + star_img.get_height() > player_pos[1]:
            if player_pos[0] < star[0] < player_pos[0] + player_img.get_width() or player_pos[0] < star[0] + star_img.get_width() < player_pos[0] + player_img.get_width():
                game_over = True

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(30)

# Game over screen
window.fill((0, 0, 0))
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, (255, 255, 255))
window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
text = font.render("Score: " + str(score), True, (255, 255, 255))
window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + text.get_height() // 2))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit the game
pygame.quit()