import pygame
pygame.init()

SCREEEN_WIDTH =800
SCREEN_HEIGHT =int(SCREEEN_WIDTH*0.9)
screen =  pygame.display.set_mode((SCREEEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("zombie shooter")



class soldier(pygame.sprite.Sprite):  #used .sprite.Sprite to use features of sprites , plain pygame wouldnt have worked
    
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        #creating a rect ->
        img = pygame.image.load('img/player/idle/0.png')
        self.img = pygame.transform.scale(img, (img.get_width()*scale , img.get_height()*scale))
        self.rect =self.img.get_rect()
        self.rect.center=(x,y)
       
player =soldier(200, 200, 2) 
# naitik =soldier(100, 100 , 3)


#----------------#

run =True
while run:
    for event in pygame.event.get():
        #quiet game
        if event.type == pygame.QUIT:
            run =False
            
    screen.blit(player.img,player.rect)
    # screen.blit(naitik.img, naitik.rect) 
    pygame.display.update()#to display it 
    # pygame.display.update()
    

pygame.quit()  