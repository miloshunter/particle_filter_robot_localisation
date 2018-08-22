# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import sys
from os import path
from parametri import *


class Simulacija:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode((SIRINA, VISINA))
        pg.display.set_caption(NASLOV)
        self.clock = pg.time.Clock()

    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.simuliraj = True
        while self.simuliraj:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.dogadjaji()
            self.azuriraj()
            self.crtaj()

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

    def azuriraj(self):
        pass

    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(BOJA_POZADINE)

        pg.display.flip()


simulacija = Simulacija()

simulacija.glavna_petlja()

