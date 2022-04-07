import pygame as pg

import DrawWindowModule
from GlobalVariable import *

class PlayerClass:
    def __init__(self):
        self.score_ = 0
        self.auto_clicks_ = 0
        self.click_qution = 1
        self.auto_click_qution = 1
        self.running = True
        self.in_store_ = False
        self.MoneyErrortime = 0

    def __call__(self, *args, **kwargs):
        return 1
    def AddScore(self, sum):
        self.score_ += sum
    def AddAutoClicks(self, sum):
        self.auto_clicks_ += sum
    # def Draw(self, win):


StoreBackGround = pg.transform.scale(pg.image.load('Pictures/StoreImages/QRYxzCA.jpeg').convert(), (100, 500))
StoreBackRect = StoreBackGround.get_rect()
StoreBackRect.topright = (WIDTH, HEIGHT // 2 - 300)

class Item:
    def __init__(self, img, cost, ability):
        self.img_ = img
        self.cost_ = cost
        self.ability_ = ability

    def draw(self, Screen, rect):
        Screen.blit(self.img_, rect)
        Screen.blit(*DrawWindowModule.MakePrice(self.cost_, rect, FontTitle))
        Screen.blit(*DrawWindowModule.MakeBonus(self.ability_, rect, FontTitle))


LightSaber = pg.transform.scale(pg.image.load('Pictures/StoreImages/+Saber.png').convert_alpha(StoreBackGround), (75, 75))

LightSaber = Item(LightSaber, 2000, "+100 autoclicks per sec")

EmpireShip = pg.transform.scale(pg.image.load('Pictures/StoreImages/SpaceShip.png').convert_alpha(StoreBackGround), (75, 75))
EmpireShip = Item(EmpireShip, 3000, "*50 click qution")

LegendaryShip = pg.transform.scale(pg.image.load('Pictures/StoreImages/LegendarySpaceShip.png').convert_alpha(StoreBackGround), (75, 75))
LegendaryShip = Item(LegendaryShip, 5000, "+228 force power")

class Store:
    def __init__(self):
        self.img_ = (StoreBackGround, StoreBackRect)
        self.items_ = [LightSaber, LightSaber, EmpireShip, EmpireShip, LegendaryShip]
    def draw(self, Screen):
        Screen.blit(*self.img_)
        for i in range(min(5, len(self.items_))):
            cord = self.img_[1].topleft
            cord = (cord[0] + 12, cord[1] + 17 + 100 * i)
            self.items_[i].draw(Screen, cord)