import pygame as pg
import DrawWindowModule as Draw
import GlobalVariable as Global


load = pg.image.load
set_scale = pg.transform.scale


class PlayerClass:
    def __init__(self):
        self.score_ = 0
        self.auto_clicks_ = 0
        self.click_quotient = 1
        self.auto_click_quotient = 1
        self.running = True
        self.in_store_ = False
        self.money_error_time = 0

    def __call__(self, *args, **kwargs):
        return 1

    def add_score(self, sum_):
        self.score_ += sum_

    def add_auto_clicks(self, sum_):
        self.auto_clicks_ += sum_


name = 'Pictures/StoreImages/StoreBackground.jpeg'
StoreBackGround = load(name).convert()
StoreBackGround = set_scale(StoreBackGround, (100, 500))
StoreBackRect = StoreBackGround.get_rect()
StoreBackRect.topright = (Global.WIDTH, Global.HEIGHT // 2 - 300)


class Item:
    def __init__(self, img, cost, ability):
        self.img_ = img
        self.cost_ = cost
        self.ability_ = ability

    def draw(self, screen, rect):
        screen.blit(self.img_, rect)
        screen.blit(*Draw.make_price(
            self.cost_, rect, Global.FontTitle))
        screen.blit(*Draw.make_bonus(
            self.ability_, rect, Global.FontTitle))


name = 'Pictures/StoreImages/Saber.png'
light_saber = load(name).convert_alpha()
light_saber = set_scale(light_saber, (75, 75))
light_saber = Item(light_saber, 2000, "+100 auto clicks per sec")

name = 'Pictures/StoreImages/SpaceShip.png'
empire_ship = load(name).convert_alpha()
empire_ship = set_scale(empire_ship, (75, 75))
empire_ship = Item(empire_ship, 3000, "*50 click quotient")

name = 'Pictures/StoreImages/LegendaryShip.png'
legendary_ship = load(name).convert_alpha()
legendary_ship = set_scale(legendary_ship, (75, 75))
legendary_ship = Item(legendary_ship, 5000, "+228 force power")


class Store:
    def __init__(self):
        self.img_ = (StoreBackGround, StoreBackRect)
        self.items_ = [light_saber, light_saber,
                       empire_ship, empire_ship,
                       legendary_ship]

    def draw(self, screen):
        screen.blit(*self.img_)
        for i in range(min(5, len(self.items_))):
            cord = self.img_[1].topleft
            cord = (cord[0] + 12, cord[1] + 17 + 100 * i)
            self.items_[i].draw(screen, cord)
