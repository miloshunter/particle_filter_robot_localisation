# Sadrzi klasu Lavirint i Zid
import pygame as pg
import parametri

class Lavirint():
    def __init__(self, simulacija):
        self.gornji_zid = Zid(simulacija, 0, 0, 768, 10)
        self.donji_zid = Zid(simulacija, 0, 758, 768, 10)
        self.levi_zid = Zid(simulacija, 0, 0, 10, 768)
        self.levi_zid = Zid(simulacija, 758, 0, 10, 768)
        self.zid1 = Zid(simulacija, 200, 0, 10, 100)
        self.zid2 = Zid(simulacija, 500, 200, 500, 10)
        self.zid3 = Zid(simulacija, 0, 350, 350, 10)
        self.zid4 = Zid(simulacija, 600, 380, 10, 500)

class Zid(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y, width, height):
        self.grupe = simulacija.svi_sprajtovi, simulacija.lavirint_sprajtovi

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.image = pg.Surface((width, height))
        self.image.fill(parametri.ZELENA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




