# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import sys
from os import path
from parametri import *
from Lavirint import Lavirint
from Robot import Robot
import threading





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
        self.tajmer_ispisa.cancel()
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
        self.svi_sprajtovi.update()


    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(BOJA_POZADINE)
        for sprajt in self.svi_sprajtovi:
            self.ekran.blit(sprajt.image, sprajt.rect)

        pg.display.flip()


simulacija = Simulacija()


def printit():
    tajmer_ispisa = threading.Timer(0.5, printit)
    simulacija.tajmer_ispisa = tajmer_ispisa
    tajmer_ispisa.setDaemon(False)
    tajmer_ispisa.start()
    print("Robot meri: " + str(simulacija.robot.laser.merenje_lasera))


try:
    printit()
except (KeyboardInterrupt, SystemExit):
    sys.exit()


simulacija.glavna_petlja()





