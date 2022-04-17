import pygame as pg


WIDTH = 1200
HEIGHT = 800
FPS = 30

pg.init()
pg.mixer.init()
Screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")


RED = (255, 0, 0)

FontTitle = pg.font.SysFont("arial", 22)
