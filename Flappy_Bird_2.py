import pygame
pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

#screen size variables
dw = 600
dh = 476
#player position
x = dw/2
y = dh/2

screen = pygame.display.set_mode([dw, dh])
pygame.display.set_caption('Flappy Bird')
pygame.display.update()
game_over = False

#grab pygame's clock
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #check if the spacebar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - 32

    #change y to simulate the square falling
    y = y + 2

    #erase drawing for new drawing
    screen.fill(black)

    #draw rectangle in relation to x and y
    pygame.draw.rect(screen, yellow, (x, y, 32, 32))
    pygame.display.update()

    #set clock to 60 frames per second
    clock.tick(60)

pygame.quit()
quit()