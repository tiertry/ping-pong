from pygame import *

win_width = 700
win_height = 500
main_win = display.set_mode((win_width, win_height))

back = (200, 255, 255)
main_win.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.sizeX = width
        self.sizeY = height
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updateR(self):
        keys = key.get_pressed() 
        if keys[K_i] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < win_height - 80:
            self.rect.y += self.speed      
    def updateL(self):
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed  

racket1 = Player('racket.png', 30,200,4,50,150)  
racket2 = Player('racket.png', 620,200,4,50,150)   
ball = GameSprite('pngwing.com.png', 325, 200, 4,50,50) 
game = True 
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        main_win.fill(back)
        racket1.updateL()
        racket2.updateR()
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()
        time.delay(50)
