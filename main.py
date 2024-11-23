from pygame import *
init()
font.init()



class GameSprtie(sprite.Sprite):
    def __init__(self, image_file,x,y,Vx,Vy):
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
        if keys[K_W]:
            self.rect.y -= self.speedy
        if keys[K_S]:
            self.rect.y += self.speedy


game = True
finish = False
win_w, win_h = 800, 600
FPS  = 53
window = display.set_mode((win_w, win_h))
font0 = font.SysFont('Arial', 50)
Player1  = Player1('')
Player2 = Player2('')

clock = time.Clock()

while game:
    display.update()


    clock.tick(FPS)



    for e in event.get():
        if e.type == QUIT :
            game = False 


    window.fill((111,0,0))