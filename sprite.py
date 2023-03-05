import pygame as p
import pygame.freetype as pf
class Ship:
    def __init__(self, speed, jpgship, x, y, damagelist, shieldlist, firelist):
        self.speed = speed
        self.jpgship = jpgship
        self.x = x
        self.y = y
        self.health = 4
        self.metsh = 0
        self.rect = jpgship.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damagelist = damagelist
        self.shieldlist = shieldlist
        self.shieldrect = shieldlist[0].get_rect()
        self.laz = 0
        self.timer = 0
        self.score = 0
        self.firelist = firelist 
        self.engine = p.image.load("assets/PNG/Parts/engine3.png")
    def draw(self, window):
        window.blit(self.jpgship, self.rect)
        if self.health == 3:
            window.blit(self.damagelist[0], self.rect)
        elif self.health == 2:
            window.blit(self.damagelist[1], self.rect)
        elif self.health == 1:
            window.blit(self.damagelist[2], self.rect)
        if self.metsh == 3:
            window.blit(self.shieldlist[2], self.shieldrect)
        elif self.metsh == 2:
            window.blit(self.shieldlist[1], self.shieldrect)
        elif self.metsh == 1:
            window.blit(self.shieldlist[0], self.shieldrect)
        window.blit(self.engine, (self.rect.x + 36, self.rect.y + 60))
    def update(self):
        control = p.key.get_pressed()
        if control[p.K_UP] == True:
            self.rect.y = self.rect.y - self.speed
        if control[p.K_DOWN] == True:
            self.rect.y = self.rect.y + self.speed
        if control[p.K_RIGHT] == True:
            self.rect.x = self.rect.x + self.speed
        if control[p.K_LEFT] == True:
            self.rect.x = self.rect.x - self.speed
        self.shieldrect.x = self.rect.x - 20
        self.shieldrect.y = self.rect.y - 20

    def damhealth(self):
        if self.metsh > 0:
            self.metsh -= 1
        else:
            self.health -= 1



class Meteor:
    def __init__(self, speedy, speedx, jpgmeteor, x, y):
        self.speedy = speedy
        self.jpgmeteor = jpgmeteor
        self.x = x
        self.y = y
        self.speedx = speedx
        self.rect = jpgmeteor.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def drawm(self, window):
            window.blit(self.jpgmeteor, self.rect)

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        self.rect.x = self.rect.x + self.speedx

class Laser:
    def __init__(self, speed, jpglaser, x, y):
        self.speed = speed
        self.jpglaser = jpglaser
        self.x = x
        self.y = y
        self.rect = jpglaser.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drawl(self, window):
            window.blit(self.jpglaser, self.rect)
            
    
    def update(self):
        self.rect.y = self.rect.y - self.speed

class Bonus:
    def __init__(self, jpgbonus, x, y, numb):
        self.jpgbonus = jpgbonus
        self.x = x
        self.y = y
        self.numb = numb
        self.rect = jpgbonus.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drawb(self, window):
        window.blit(self.jpgbonus, self.rect)

class Button:
    def __init__(self, button, x, y, text, a, b):
        self.button = button
        self.text = text
        self.rect = button.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.txt = pf.Font("Bonus/kenvector_future_thin.ttf", 25)
        self.a = a
        self.b = b
    def draw(self, window):

        window.blit(self.button, self.rect)
        self.txt.render_to(window, (self.rect.x + self.a, self.rect.y + self.b), self.text)

class Fire:
    def __init__(self, firelist, x, y):
        self.firelist = firelist
        self.firerect = firelist[0].get_rect()
        self.firerect.x = x
        self.firerect.y = y
        self.change = 0
        
    
    def draw(self, target_surf):
        target_surf.blit(self.firelist[int(self.change)], self.firerect)

    def update(self, speed):
        a = len(self.firelist)
        self.change += speed
        if self.change >= a:
            self.change = 0

