import pygame, random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

flappyBird = pygame.image.load("flappyBird.png")
background = pygame.image.load("background.png")

dw = 600
dh = 476
pillarWidth = 80
screen = pygame.display.set_mode([dw, dh])
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

def createNewPillars(pillars):
    newPillars = []
    top = pygame.__rect_constructor(dw,0,pillarWidth,random.randrange(100,250))
    bottomPillarHeight = random.randrange(200,300)
    bottom = pygame.__rect_constructor(dw,dh-(bottomPillarHeight/2),pillarWidth,bottomPillarHeight)
    newPillars.append(top)
    newPillars.append(bottom)
    pillars.append(newPillars)


def collisionDetect(pillars,player):
    for p in pillars:
        if player.colliderect(p[0]):
            return True
        elif player.colliderect(p[1]):
            return True

    return False

def message(msg, color,x,y):
    font_style = pygame.font.SysFont(None, 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])
    pygame.display.update()


def gameLoop():
    x = dw / 2
    y = dh / 2
    pillars = []
    score = 0
    pillarsPassed = []
    game_over = False
    close_game = False
    addPillars = pygame.USEREVENT + 1
    pygame.time.set_timer(addPillars, 5000)
    createNewPillars(pillars)

    player = pygame.__rect_constructor(dw / 2, y, 32, 32);
    while not close_game:
        while game_over:
            message("Your Score is " + str(len(pillarsPassed)), red, dw/2, dh/2)
            message("Tap Space Bar to Play again", red, dw/6, dh/3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close_game = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.y -= 32
            if event.type == addPillars:
                createNewPillars(pillars)
                pygame.time.set_timer(addPillars,5000)
        # screen.fill(black)

        screen.blit(background, (0,0))
        # pygame.draw.rect(screen, yellow, player)
        screen.blit(flappyBird,player)
        for p in pillars:
            p[0].x -= 1
            p[1].x -= 1
            if player.x > p[0].x and p[0] not in pillarsPassed:
                pillarsPassed.append(p[0])
            if p[0].x < -80:
                del pillars[0]
            pygame.draw.rect(screen,green,p[0])
            pygame.draw.rect(screen,green,p[1])
        pygame.display.update()
        player.y += 2
        if collisionDetect(pillars,player):
            game_over = True
        if player.y > dh-30 or player.y < 0:
            game_over = True
        clock.tick(60)
    pygame.quit()
    quit()

gameLoop()