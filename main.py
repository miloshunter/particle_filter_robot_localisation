# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import sys
from os import path
from parametri import *
from Lavirint import Lavirint
from Robot import Robot


class Simulacija:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode((SIRINA, VISINA))
        pg.display.set_caption(NASLOV)
        self.clock = pg.time.Clock()
        self.nova_simulacija()

    def nova_simulacija(self):
        self.svi_sprajtovi = pg.sprite.Group()
        self.lavirint_sprajtovi = pg.sprite.Group()

        self.lavirint = Lavirint(self)

        self.robot = Robot(self, 200, 200)


    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.simuliraj = True
        while self.simuliraj:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.dogadjaji()
            self.crtaj()
            self.azuriraj()


    def izadji(self):
        pg.quit()
        sys.exit()

    def dogadjaji(self):
        for dogadjaj in pg.event.get():
            if dogadjaj.type == pg.QUIT:
                self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_ESCAPE:
                    self.izadji()
                # self.robot.get_keys()

    def azuriraj(self):
        self.svi_sprajtovi.update()


    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(BOJA_POZADINE)
        for sprajt in self.svi_sprajtovi:
            self.ekran.blit(sprajt.image, sprajt.rect)

        pg.display.flip()


simulacija = Simulacija()

simulacija.glavna_petlja()


