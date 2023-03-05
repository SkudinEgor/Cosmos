import pygame as p


class Frog:
    def __init__(self):
        self.froglist = []
        for fr in range(1, 11):
            jpgfrog = p.image.load(F"FrogEgor/attack_{fr}.png")
            self.froglist.append(jpgfrog)
        self.rect = p.Rect(10, 200, self.froglist[0].get_width(), self.froglist[0].get_height())
        self.change = 0   
    def animate(self):
        pass

    def draw(self, target_surf):
        target_surf.blit(self.froglist[self.change], self.rect)

    def update(self, speed):
        self.change += 1
        if self.change == 10:
            self.change = 0
    


SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

p.init()
clock = p.time.Clock()
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption('Frog')

frog = Frog()



running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN
                                    and event.key == p.K_ESCAPE):
            running = False


    screen.fill((255, 255, 255))

    frog.update(0.25)
    frog.draw(screen)

    clock.tick(60)
    p.display.flip()

