from pygame import *
init()
font.init()
from random import randint




class GameSprtie(sprite.Sprite):
    def __init__(self, image_file,x,y,w,h,speedx,speedy):
        self.image = transform.scale(image.load(image_file), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

class Player2(GameSprtie):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speedy
        if keys[K_DOWN]:
            self.rect.y += self.speedy



class Player1(GameSprtie):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speedy
        if keys[K_s]:
            self.rect.y += self.speedy

class Ball(GameSprtie):
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if (self.rect.y <= 0) or (self.rect.y >= win_h):
            self.speedy = -self.speedy

        if sprite.collide_rect(self,player1):
            self.speedx = abs(self.speedx)
        if sprite.collide_rect(self,player2):
            self.speedx = -abs(self.speedx)

        global score1, score2
        if self.rect.x <= 0:
            score2 +=1
            self.rect.x = win_w//2
            self.rect.y = win_h//2
        if self.rect.x >= win_w:
            score1 += 1
            self.rect.x = win_w//2
            self.rect.y = win_h//2



#image_file,x,y,w,h,speedx,speedy
player1 = Player1('gffg.png',5,300,40,250,10,10)
player2 = Player2('gffg.png',730,300,40,250,10,10)
ball = Ball('мина.jpg',300,10 ,40,40,10,10)

game = True
finish = False
win_w, win_h = 800, 600
FPS  = 53
window = display.set_mode((win_w, win_h))
font0 = font.SysFont('Arial', 50)
score1 = 0
score2 = 0

clock = time.Clock()

while game:
    display.update()

    player1.update()
    player2.update()
    ball.update()
    
    image_score1 = font0.render('Игрок1 :'+str(score1), True, (50,50,50))
    image_score2 = font0.render('Игрок2 :'+str(score2), True, (50,50,50))


    clock.tick(FPS)



    for e in event.get():
        if e.type == QUIT :
            game = False 
        elif e.type == KEYDOWN and e.key == K_r:
            player1 = Player1('gffg.png',5,300,40,250,10,10)
            player2 = Player2('gffg.png',730,300,40,250,10,10)
            ball = Ball('мина.jpg',300,10 ,40,40,10,10)
        elif e.type == KEYDOWN and e.key == K_0:
            ball = Ball('мина.jpg',300,10 ,40,40,10,10)




    window.fill((238 ,223, 204))

    player1.reset()
    player2.reset()
    ball.reset()
    window.blit(image_score1, (10,20))
    window.blit(image_score2, (600,20))

 