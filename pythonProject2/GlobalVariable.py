import pygame as pg

WIDTH = 1200
HEIGHT = 800
FPS = 30


pg.init()
pg.mixer.init()
Screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


FontTitle = pg.font.SysFont("arial", 22)
MiniTitle = pg.font.SysFont("arial", 18)

