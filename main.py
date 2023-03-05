import pygame as p
import settings as s
import sprite as sp
import random as r
import pygame.freetype as pf
p.init()
window = p.display.set_mode((s.WIDTH, s.HEIGHT))
close = 2
clock = p.time.Clock()


jpgbonusl = p.image.load("assets/PNG/Power-ups/bolt_silver.png")
jpgship = p.image.load("assets/PNG/playerShip1_blue.png")
jpgmeteor = p.image.load("assets/PNG/Meteors/meteorBrown_big3.png")
jpglaser = p.image.load("assets/PNG/Lasers/laserBlue01.png")
jpgmenu = p.image.load("assets/Backgrounds/blue.png")
jpgback = p.image.load("assets/Backgrounds/purple.png")
jpgmenu = p.transform.scale(jpgmenu, (s.WIDTH, s.HEIGHT))
jpgback = p.transform.scale(jpgback, (s.WIDTH, s.HEIGHT))
jpgbonusshield = p.image.load("assets/PNG/Power-ups/powerupBlue_shield.png")
jpgbonushealth = p.image.load("assets/PNG/Power-ups/pill_red.png")
jpgbonusstar = p.image.load("assets/PNG/Power-ups/powerupYellow_star.png")
jpgbutton = p.image.load("assets/PNG/UI/buttonGreen.png")
jpgbutton2 = p.image.load("assets/PNG/UI/buttonRed.png")
shieldlist = []
jpgbonuslist = [jpgbonushealth, jpgbonusshield, jpgbonusl, jpgbonusstar]
firelist = []
for fire in range(11, 18):
    jpgfire = p.image.load(F"assets/PNG/Effects/fire{fire}.png")
    firelist.append(jpgfire)



for sh in range(1, 4):
    jpgsh = p.image.load(F"assets/PNG/Effects/shield{sh}.png")
    shieldlist.append(jpgsh)
damagelist = []
for dam in range(1, 4):
    jpgdamage = p.image.load(F"assets/PNG/Damage/playerShip1_damage{dam}.png")
    damagelist.append(jpgdamage)
spaceship = sp.Ship(2, jpgship, s.WIDTH / 2, s.HEIGHT / 2, damagelist, shieldlist, firelist)
button = sp.Button(jpgbutton, 325, 375, "Start the game", 5, 13)
button2 = sp.Button(jpgbutton2, 975, 375, "Exit", 80, 13 )
fire = sp.Fire(firelist, spaceship.rect.x + 42, spaceship.rect.y + 75)
timer = 0
text = pf.Font("Bonus/kenvector_future.ttf", 50)
text2 = pf.Font("Bonus/kenvector_future.ttf", 50)
pause = 0
def colid():
    for col in meteoridlist:
        if col.rect.colliderect(spaceship.rect) == True:
            spaceship.damhealth()
            meteoridlist.remove(col)

          

    for col in meteoridlist:
        for collaz in lazerlist:
            if collaz.rect.colliderect(col.rect) == True:
                meteoridlist.remove(col)
                lazerlist.remove(collaz)
                spaceship.score += 1

            

def bonusa():
    for bon in bonuslist:
        if bon.rect.colliderect(spaceship.rect) == True:
            if bon.numb == 1:
                spaceship.metsh = 3
            if bon.numb == 0:
                spaceship.health += 1
            if bon.numb == 2:
                meteoridlist.clear()
            if bon.numb == 3:
                spaceship.laz = 1
                spaceship.timer = p.time.get_ticks()   
            bonuslist.clear()
bonuslist = []
TIMEB = p.USEREVENT + 1
p.time.set_timer(TIMEB, 3000)
TIMEH = p.USEREVENT + 2
p.time.set_timer(TIMEH, 2000)


lazerlist = []
TIMEM =  p.USEREVENT
p.time.set_timer(TIMEM, 500)
meteoridlist = []

while 1 + 1 == close:
    event = p.event.get()
    for element in event:
        if element.type == p.QUIT:
            close = 3

        if element.type == p.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(element.pos) == True:
                pause = 1
                spaceship.health = 4
                spaceship.score = 0
                meteoridlist.clear()
                lazerlist.clear()
                bonuslist.clear()
            if button2.rect.collidepoint(element.pos) == True:
                close = 3
            
        if element.type == p.KEYDOWN:
            if element.key == p.K_RETURN:
                lazer = sp.Laser(3, jpglaser, spaceship.rect.x, spaceship.rect.y)
                lazerlist.append(lazer)
                if spaceship.laz == 1:
                    lazer2 = sp.Laser(3, jpglaser, spaceship.rect.right, spaceship.rect.y)
                    lazerlist.append(lazer2)
        if element.type == TIMEM:
            meteorid = sp.Meteor(r.randint(1, 5), r.randint(-5, 5), jpgmeteor, r.randint(0, s.WIDTH), 0)
            meteoridlist.append(meteorid)
        if element.type == TIMEB:
            c = r.randint(0, 3)
            a = jpgbonuslist[c]
            bonus = sp.Bonus(a, r.randint(0, s.WIDTH), r.randint(0, s.HEIGHT), c)
            bonuslist.clear()
            bonuslist.append(bonus)

    fire.firerect.x = spaceship.rect.x + 42
    fire.firerect.y = spaceship.rect.y + 75
    bonusa()
        
    
    
    if p.time.get_ticks() // 1000 - spaceship.timer // 1000 == 7:
        spaceship.laz = 0

    
    
    if spaceship.health == 0:
        pause = 0
    colid()






    if pause == 1:
        window.blit(jpgback, (0, 0))
        spaceship.draw(window)
        for a in lazerlist:
            a.drawl(window)
            a.update()
        spaceship.update()
        for b in meteoridlist:
            b.drawm(window)
            b.update()
        for c in bonuslist:
            c.drawb(window)
        text.render_to(window, (100, 100), F"Your healths:{spaceship.health}")
        text.render_to(window, (100, 60), F"Your score:{spaceship.score}")
        fire.update(0.1)
        fire.draw(window)
    else:
        window.blit(jpgmenu, (0, 0))
        button.draw(window)
        button2.draw(window)
        text2.render_to(window, (450, 10), "Cosmosbattle", (39, 82, 225)) 
        


    p.display.update()
    clock.tick(156)