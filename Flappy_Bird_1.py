import pygame
pygame.init()

#create some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

#set screen properties
screen = pygame.display.set_mode([600, 476])
pygame.display.set_caption('Flappy Bird')
pygame.display.update()
game_over = False

# game loop
while not game_over:
    #collection of events that occur at once (i.e. pressing two keys at the same time)
    for event in pygame.event.get():
        #when user hits the X button on the window
        if event.type == pygame.QUIT:
            game_over = True
    #drawing a square
    pygame.draw.rect(screen, yellow, (300, 200, 32, 32))
    pygame.display.update()

pygame.quit()
quit()