import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase Game")

# Load images
rocket_img = pygame.image.load('rocket.png')
bad_guy_img = pygame.image.load('bad_guy.png')

# Scale images
rocket_img = pygame.transform.scale(rocket_img, (150, 150))
bad_guy_img = pygame.transform.scale(bad_guy_img, (100, 100))

# Player classes
class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = rocket_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

class BadGuy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bad_guy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = 1.3

    def update(self):
        # Move towards the rocket
        if self.rect.x < rocket.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > rocket.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < rocket.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > rocket.rect.y:
            self.rect.y -= self.speed

# Timer class
class Timer:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()

    def get_time(self):
        return (pygame.time.get_ticks() - self.start_time) // 1000

# Create sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create objects
rocket = Rocket()
bad_guy = BadGuy()
timer = Timer()

# Add objects to sprite groups
all_sprites.add(rocket, bad_guy)
players.add(rocket)
enemies.add(bad_guy)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(rocket, enemies, False)
    if hits:
        # Rocket collided with the bad guy
        bad_guy.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        pygame.time.delay(1000)  # Delay before the bad guy resumes chasing

    # Draw
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Display timer
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {timer.get_time()} seconds", True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
