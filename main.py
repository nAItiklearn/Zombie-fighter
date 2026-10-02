import pygame
pygame.init()

SCREEEN_WIDTH =800
SCREEN_HEIGHT =int(SCREEEN_WIDTH*0.9)

screen =  pygame.display.set_mode((SCREEEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("zombie shooter")

run =True
while run:
    for event in pygame.event.get():
        #quiet game
        if event.type == pygame.QUIT:
            run =False

pygame.quit()