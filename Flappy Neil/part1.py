import pygame
import sys
screen_width = 800
screen_height = 800 
pygame.init()
pygame.display.set_caption('Flappy NEIL')
screen = pygame.display.set_mode((screen_height,screen_width))
bird = pygame.image.load('/Users/lung/Desktop/preply/Flappy Neil/neil.png')
bg = pygame.image.load('/Users/lung/Desktop/preply/Flappy Neil/bg.jpeg')
bg2 = pygame.image.load('/Users/lung/Desktop/preply/Flappy Neil/bg2.jpeg')

bird_rect = bird.get_rect() 
bird_rect.topleft = (50,50)

gravity = 0.005  
bird_velocity = 0
jump_height = -2
inc = 0 
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_height
                print(bird_velocity)

            if event.key == pygame.K_RIGHT:
                bird_rect.topleft = bird_rect.topleft 
                inc = inc + 30
                bird_rect.topleft = inc,bird_rect.bottom 
            if event.key == pygame.K_LEFT:
                bird_rect.topleft = bird_rect.topleft 
                inc = inc - 30
                bird_rect.topleft = inc,bird_rect.bottom 



    # apply gravity     
    bird_velocity += gravity
    bird_rect.y += bird_velocity

    if bird_rect.bottom >= screen_height:
        bird_rect.bottom = screen_height
        bird_velocity = 0
    elif bird_rect.top < 0:
        bird_rect.top = 0
        bird_velocity = 0

    screen.blit(bg2,(0,0))
    screen.blit(bg,(0,0))

    screen.blit(bird, bird_rect)
    pygame.display.flip()

            
pygame.quit()
sys.exit()

   