import random
import math
import sys
import pygame as pg
import UpdateAndCheck as UC
from GlobalVariable import *
import Store
import Player
import DrawWindowModule


clock = pg.time.Clock()
# Surface = pg.Surface([640,480], pg.SRCALPHA, 32)


BackGroundImage = pg.image.load('Pictures/DeathStar.png').convert()
BackGroundImage = pg.transform.scale(BackGroundImage, (WIDTH, HEIGHT))
rect = BackGroundImage.get_rect()
rect.center = (600, 350)
DarthVaderImage = pg.image.load('Pictures/DarthVader/darth-vader-sheev-palpatine-luke-skywalker-r2-d2-general-grievous-png-favpng-c6SHfMDgB0T3zkcZQt9Vep1DF.jpg').convert_alpha()
DarthVaderImage = pg.transform.scale(DarthVaderImage, (400, 500))
Vader_rect = DarthVaderImage.get_rect()
Vader_rect.center = (600, 500)

BitcoinImage = pg.transform.scale(pg.image.load('Pictures/unnamed.png').convert_alpha(), (50, 50))
BitcoinRect = BitcoinImage.get_rect()
BitcoinRect.center = (50, 25)

StoreIconImage = pg.transform.scale(pg.image.load('Pictures/Store.png').convert_alpha(), (200, 150))
StoreIconRect = StoreIconImage.get_rect()
StoreIconRect.topleft = (1000, 600)

Screen.blit(BackGroundImage, rect)


player_ = Player.PlayerClass()
store = Player.Store()

def DrawGeneralWin(player_):
    Screen.blit(BackGroundImage, rect)
    Screen.blit(DarthVaderImage, Vader_rect)
    Screen.blit(BitcoinImage, BitcoinRect)

    Screen.blit(*DrawWindowModule.MakeScoreTitle(int(player_.score_), FontTitle))
    Screen.blit(*DrawWindowModule.MakeAutoClickTitle(player_.auto_clicks_, FontTitle))
    Screen.blit(StoreIconImage, StoreIconRect)


def DrawWindow(player_):
    DrawGeneralWin(player_)

    if player_.in_store_:
        store.draw(Screen)

    if(player_.MoneyErrortime):
        player_.MoneyErrortime -= 1
        DrawWindowModule.print_text("You haven't enough money", Screen, FontTitle)

    pg.display.update()


while player_.running:
    clock.tick(FPS)

    UC.CheckEvents(player_)
    UC.Update(player_)
    DrawWindow(player_)

pg.quit()
sys.exit()
