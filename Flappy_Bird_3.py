import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

dw = 600
dh = 476
x = dw/2
y = dh/2

screen = pygame.display.set_mode([dw, dh])
pygame.display.set_caption('Flappy Bird')
pygame.display.update()
game_over = False

clock = pygame.time.Clock()

#create Pillars
pillars = []

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - 32
    y = y + 2

    screen.fill(black)
    pygame.draw.rect(screen, yellow, (x, y, 32, 32))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()