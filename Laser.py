# Klasa za robota koji ce ici po lavirintu i meriti
import pygame as pg
import pygame.gfxdraw
import parametri
import copy
import math
vec = pg.math.Vector2



class Laser(pg.sprite.Sprite):
    def __init__(self, robot):
        pg.sprite.Sprite.__init__(self, robot.simulacija.svi_sprajtovi)

        ATOM_IMG = pg.Surface((parametri.SIRINA, parametri.VISINA), pg.SRCALPHA)
        self.robot = robot
        self.simulacija = robot.simulacija
        self.image = ATOM_IMG
        self.rect = self.image.get_rect()

    def update(self):
        def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
            xr = math.cos(theta) * (x - xo) - math.sin(theta) * (y - yo) + xo
            yr = math.sin(theta) * (x - xo) + math.cos(theta) * (y - yo) + yo
            return [xr, yr]

        razdaljina_od_centra = parametri.DUZINA_ROBOTA/2
        pozicija1 = copy.deepcopy(self.robot.pos)

        pozicija2 = copy.deepcopy(self.robot.pos)
        pozicija2 += (razdaljina_od_centra*10, 0)
        pozicija2[0], pozicija2[1] = rotate(pozicija2[0], pozicija2[1],
                                            self.robot.rect.center[0],
                                            self.robot.rect.center[1],
                                            -self.robot.rot*3.14/180)

        levo = min(pozicija1[0], pozicija2[0])
        desno = max(pozicija1[0], pozicija2[0])
        gore = min(pozicija1[1], pozicija2[1])
        dole = max(pozicija1[1], pozicija2[1])

        self.rect = pg.Rect(0, 0, parametri.SIRINA, parametri.VISINA)

        ATOM_IMG = pg.Surface((parametri.SIRINA, parametri.VISINA), pg.SRCALPHA)
        self.image = ATOM_IMG

        bottomleft = self.simulacija.lavirint.zidovi[0].rect.bottomleft
        bottomright = self.simulacija.lavirint.zidovi[0].rect.bottomright
        topleft = self.simulacija.lavirint.zidovi[0].rect.topleft
        topright = self.simulacija.lavirint.zidovi[0].rect.topright

        intersection = self.measure_distance(pozicija1[0], pozicija1[1], pozicija2[0], pozicija2[1],
                              bottomleft[0], bottomleft[1], bottomright[0], bottomright[1])

        crtaj_do = pozicija2
        if intersection:
            pg.draw.circle(self.image, parametri.BELA, (intersection[0],
                                                          intersection[1]),
                           3)
            crtaj_do = intersection

        pg.draw.line(self.image, parametri.CRVENA, pozicija1, crtaj_do)



    def measure_distance(self, x1, y1, x2, y2, x3, y3, x4, y4):
        def lineLine(x1, y1, x2, y2, x3, y3, x4, y4):
            #  Calculate direction of the lines
            try:
                uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) /\
                     ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
            except ZeroDivisionError:
                return 0
            try:
                uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) /\
                     ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
            except ZeroDivisionError:
                return 0

            if uA >= 0 and uA <=1 and uB >= 0 and uB <=1:
                intersectionX = int(x1 + (uA * (x2-x1)))
                intersectionY = int(y1 + (uA * (y2 - y1)))

                return intersectionX, intersectionY
            else:
                return None

        return lineLine(x1, y1, x2, y2, x3, y3, x4, y4)