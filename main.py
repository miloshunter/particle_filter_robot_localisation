# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import sys
from os import path
import random
import parametri
from Lavirint import Lavirint
from Robot import Robot
import threading
from Partikl import Partikl


class Simulacija:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode((parametri.SIRINA, parametri.VISINA))
        pg.display.set_caption(parametri.NASLOV)
        self.clock = pg.time.Clock()
        self.partikli = []
        self.nova_simulacija()

    def nova_simulacija(self):
        self.svi_sprajtovi = pg.sprite.Group()
        self.lavirint_sprajtovi = pg.sprite.Group()
        self.lavirint = Lavirint(self)
        self.robot = Robot(self, 200, 200)
        while len(self.partikli) < parametri.BROJ_PARTIKALA:
            self.kreiraj_partikl((10, 768), (10, 768), (0, 360))

    def kreiraj_partikl(self, randrange_x, randrange_y, randrange_angle):
        novi_partikl = Partikl(self, random.randrange(max(10, randrange_x[0]), min(768, randrange_x[1])),
                               random.randrange(max(10, randrange_y[0]), min(768, randrange_y[1])),
                               random.randrange(randrange_angle[0], randrange_angle[1]))
        if pg.sprite.spritecollide(novi_partikl, self.svi_sprajtovi, False):
            self.partikli.append(novi_partikl)
        else:
            novi_partikl.remove(self.svi_sprajtovi)

    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.simuliraj = True
        while self.simuliraj:
            self.dt = self.clock.tick(parametri.FPS) / 1000.0
            self.dogadjaji()
            self.crtaj()
            self.azuriraj()

    def izadji(self):
        self.tajmer_ispisa.cancel()
        pg.quit()
        sys.exit()

    def algoritam(self):
        partikli = simulacija.partikli

        izmerio_robot = simulacija.robot.laser.merenje_lasera

        partikli_za_uklanjanje = []
        for partikl in partikli:
            izmerio_partikl = partikl.laser.merenje_lasera
            if izmerio_partikl < izmerio_robot - 40 or izmerio_partikl > izmerio_robot + 40:
                simulacija.svi_sprajtovi.remove(partikl.laser)
                partikli_za_uklanjanje.append(partikl)
                simulacija.svi_sprajtovi.remove(partikl)
        for partikl in partikli_za_uklanjanje:
            partikli.remove(partikl)

        if len(partikli) > 0:
            while len(partikli) < parametri.BROJ_PARTIKALA:
                indeks = random.randrange(len(partikli))

                self.kreiraj_partikl((int(partikli[indeks].pos[0]-50), int(partikli[indeks].pos[0]+50)),
                                     (int(partikli[indeks].pos[1] - 50), int(partikli[indeks].pos[1] + 50)),
                                     (int(partikli[indeks].rot-10), int(partikli[indeks].rot+10)))
        else:
            while len(self.partikli) < parametri.BROJ_PARTIKALA:
                self.kreiraj_partikl((10, 768), (10, 768), (0, 360))

    def dogadjaji(self):
        for dogadjaj in pg.event.get():
            if dogadjaj.type == pg.QUIT:
                self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_ESCAPE:
                    self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_SPACE:
                    self.algoritam()

    def azuriraj(self):
        self.svi_sprajtovi.update()


    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(parametri.BOJA_POZADINE)
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





