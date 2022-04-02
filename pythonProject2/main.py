import random
import math
import sys
import pygame as pg
import UpdateAndCheck as UC
from GlobalVariable import *
import Store
import Player
import DrawWindowModule


pg.init()
pg.mixer.init()
Screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

BackGroundImage = pg.image.load('Pictures/DeathStar.png').convert()
BackGroundImage = pg.transform.scale(BackGroundImage, (WIDTH, HEIGHT))
rect = BackGroundImage.get_rect()
rect.center = (600, 350)
DarthVaderImage = pg.image.load('Pictures/DarthVader/Vader-removebg-preview.png').convert()
DarthVaderImage = pg.transform.scale(DarthVaderImage, (400, 500))
Vader_rect = DarthVaderImage.get_rect()
Vader_rect.center = (600, 500)

BitcoinImage = pg.transform.scale(pg.image.load('Pictures/unnamed.png').convert(), (50, 50))
BitcoinRect = BitcoinImage.get_rect()
BitcoinRect.center = (1075, 25)

StoreImage = pg.transform.scale(pg.image.load('Pictures/Store.png').convert(), (200, 150))
StoreRect = StoreImage.get_rect()
StoreRect.topleft = (1000, 600)

Screen.blit(BackGroundImage, rect)
FontTitle = pg.font.SysFont("arial", 22)
MiniTitle = pg.font.SysFont("arial", 18)

player_ = Player.PlayerClass()


StoreBackGround = pg.transform.scale(pg.image.load('Pictures/StoreImages/QRYxzCA.jpeg').convert(), (100, 500))
StoreBackRect = StoreBackGround.get_rect()
StoreBackRect.topright = (WIDTH, HEIGHT // 2 - 300)

LightSaber = pg.transform.scale(pg.image.load('Pictures/StoreImages/+Saber.png').convert(), (75, 75))
SaberRect = StoreBackGround.get_rect()
SaberRect.center = (WIDTH - 35, HEIGHT // 2 - 30)


def DrawStore():
    Screen.blit(StoreBackGround, StoreBackRect)

    Screen.blit(LightSaber, SaberRect)
    Screen.blit(*DrawWindowModule.MakeBonus(100, SaberRect, MiniTitle))
    Screen.blit(*DrawWindowModule.MakePrice(2000, SaberRect, MiniTitle))



def DrawWindow(player_):
    Screen.blit(BackGroundImage, rect)
    Screen.blit(DarthVaderImage, Vader_rect)
    BitcoinRect.center = (50, 25)
    Screen.blit(BitcoinImage, BitcoinRect)

    Screen.blit(*DrawWindowModule.MakeScoreTitle(player_.score_, FontTitle))
    Screen.blit(*DrawWindowModule.MakeAutoClickTitle(player_.auto_clicks_, FontTitle))
    Screen.blit(StoreImage, StoreRect)

    if player_.in_store_:
        DrawStore()

    if(player_.MoneyErrortime):
        player_.MoneyErrortime -= 1
        DrawWindowModule.print_text("You haven't enough money", Screen, MiniTitle)

    pg.display.update()


while player_.running:
    clock.tick(FPS)

    UC.CheckEvents(player_)
    UC.Update(player_)
    DrawWindow(player_)

pg.quit()
sys.exit()
