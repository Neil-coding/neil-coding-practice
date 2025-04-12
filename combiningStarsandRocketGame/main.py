import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 1000
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neil's Mission Rocket")

# Load background image
background_image = pygame.image.load("bg.jpeg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load rocket image
rocket_image = pygame.image.load("rocketnbg.png")
rocket_image = pygame.transform.scale(rocket_image, (100, 100))
rocket_rect = rocket_image.get_rect()
rocket_rect.centerx = WIDTH // 2
rocket_rect.bottom = HEIGHT - 20

# Load bullet image
bullet_image = pygame.image.load("happy.png")
bullet_image = pygame.transform.scale(bullet_image, (20, 20))

# Rocket speed
ROCKET_SPEED = 30

# Bullet speed
BULLET_SPEED = 20

# Star speed
STAR_SPEED = 1

# Star creation function
def create_star():
    star = {
        'image': pygame.image.load("images/star1.png"),
        'rect': pygame.Rect(random.randint(0, WIDTH - 25), 0, 25, 25),
    return star
    }

# Star list
star_list = []

# Initialize stars
for _ in range(5):
    star_list.append(create_star())

# Bullet list
bullets = []

# Game settings
clock = pygame.time.Clock()
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket_rect.x -= ROCKET_SPEED
            elif event.key == pygame.K_RIGHT:
                rocket_rect.x += ROCKET_SPEED
            elif event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet_rect.centerx = rocket_rect.centerx
                bullet_rect.bottom = rocket_rect.top
                bullets.append(bullet_rect)
        

    window.blit(background_image, (0, 0))

    # Move and draw stars
    for star in star_list:
        star['rect'].y += STAR_SPEED
        if star['rect'].y > HEIGHT:
            star['rect'].y = 0
            star['rect'].x = random.randint(0, WIDTH - 25)
        window.blit(star['image'], star['rect'])

    # Move and draw rocket
    window.blit(rocket_image, rocket_rect)

    # Move and draw bullets
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        window.blit(bullet_image, bullet)

    # Collision detection
    for bullet in bullets[:]:
        for star in star_list[:]:
            if bullet.colliderect(star['rect']):
                bullets.remove(bullet)
                star_list.remove(star)
                score += 1
                star_list.append(create_star())
                
    for star in star_list:
        if rocket_rect.colliderect(star['rect']):
            running = False

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
