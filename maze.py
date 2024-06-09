#створи гру "Лабіринт"!
from pygame import *

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
wn = display.set_mode((700, 500))
display.set_caption("Лабіринт-Логіка")
clock = time.Clock()
game = True
finish = False
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
    
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-60 :
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 0 :
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < 700-60 :
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "up"
    def update(self):
        if self.rect.y < 0:
            self.direction = "down"
        if self.rect.y > 400:
            self.direction = "up"

        if self.direction == "up":
            self.rect.y -= self.speed
        if self.direction == "down":
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y,wall_width,wall_height,color):
        self.color = color
        self.height = wall_height
        self.width = wall_width
        self.image = Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
color_wall = (23,54,101)
player = Hero("hero.png", 100,100,60,60,5)
enemy = Enemy("cyborg.png", 200,200,60,60,5)
wall1 = Wall(0,0,20,700,(23,54,101))
wall2 = Wall(0,0,700,20,(23,54,101))
wall3 = Wall(700-20,0,20,500,color_wall)
wall4 = Wall(0,500-20,700,20,color_wall)
background = transform.scale(image.load("background.jpg"),(700,500))
while game:
    wn.blit(background,(0,0))
    player.reset()
    player.update()
    enemy.reset()
    enemy.update()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)