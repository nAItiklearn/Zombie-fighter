import pygame
pygame.init()

SCREEEN_WIDTH =800
SCREEN_HEIGHT =int(SCREEEN_WIDTH*0.9)
screen =  pygame.display.set_mode((SCREEEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("zombie shooter")

BG = (123, 201, 120)
def draw_bg():
    screen.fill(BG)

#set framerate
clock = pygame.time.Clock()
FPS =60
class soldier(pygame.sprite.Sprite):  #used .sprite.Sprite to use features of sprites , plain pygame wouldnt have worked
    
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        #speed
        self.speed=speed
        #creating a rect ->
        img = pygame.image.load('img/player/idle/0.png')
        self.img = pygame.transform.scale(img, (img.get_width()*scale , img.get_height()*scale))
        self.rect =self.img.get_rect()
        self.rect.center=(x,y)
        
    def move(self, moving_left, moving_right):
        dx = 0  #using delta variables so that we could find the exact position of the sprite , useful in colisions
        dy =0
        #assign movn variables
        if moving_left:
            dx=-self.speed
        if moving_right:
            dx=+self.speed
            
        #update pos
        self.rect.x +=dx
        self.rect.y+=dy
        
        
    def draw(self):
        screen.blit(self.img, self.rect)
       
player =soldier(200, 200, 2, 4) 
# naitik =soldier(100, 100 , 3)

MOVING_LEFT = False
MOVING_RIGHT =False

#----------------#

run =True
while run:
    clock.tick(FPS)
    draw_bg()
    
    
    player.draw()
    player.move(MOVING_LEFT, MOVING_RIGHT)
    for event in pygame.event.get():
        #quiet game
        if event.type == pygame.QUIT:
            run =False
        #controls  (key pressed)
        if event.type ==pygame.KEYDOWN:
            
            if event.key ==pygame.K_a:
                MOVING_LEFT=True
            if event.key ==pygame.K_d:
                MOVING_RIGHT= True
            #exit by esc
            if event.key ==pygame.K_ESCAPE:
                run=False
        #key removed
        if event.type==pygame.KEYUP:
            if event.key ==pygame.K_a:
                MOVING_LEFT=False
            if event.key ==pygame.K_d:
                MOVING_RIGHT = False
        
       
        
        
        
                
            
    
    pygame.display.update()
pygame.quit()  