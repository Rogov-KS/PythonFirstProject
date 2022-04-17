import sys
import pygame as pg
import UpdateAndCheck as Uc
import GlobalVariable as Global
import Player
import DrawWindowModule as Draw


clock = pg.time.Clock()
Screen = Global.Screen
load = pg.image.load
set_scale = pg.transform.scale

player_ = Player.PlayerClass()
store = Player.Store()

BackGroundImage = load('Pictures/DeathStar.png').convert()
BackGroundImage = set_scale(BackGroundImage, (Global.WIDTH, Global.HEIGHT))
rect = BackGroundImage.get_rect()
rect.center = (600, 350)
DarthVaderImage = load('Pictures/Vader.png').convert_alpha()
DarthVaderImage = set_scale(DarthVaderImage, (400, 500))
Vader_rect = DarthVaderImage.get_rect()
Vader_rect.center = (550, 500)

BitcoinImage = load('Pictures/Bitcoin.png').convert_alpha()
BitcoinImage = set_scale(BitcoinImage, (50, 50))
BitcoinRect = BitcoinImage.get_rect()
BitcoinRect.center = (50, 35)

StoreIconImage = load('Pictures/Store.png').convert_alpha()
StoreIconImage = set_scale(StoreIconImage, (200, 150))
StoreIconRect = StoreIconImage.get_rect()
StoreIconRect.topleft = (980, 600)

Screen.blit(BackGroundImage, rect)


def draw_general_win(player_):
    Screen.blit(BackGroundImage, rect)
    Screen.blit(DarthVaderImage, Vader_rect)
    Screen.blit(BitcoinImage, BitcoinRect)

    Screen.blit(*Draw.make_score_title(
        int(player_.score_), Global.FontTitle))
    Screen.blit(*Draw.make_auto_click_title(
        player_.auto_clicks_, Global.FontTitle))
    Screen.blit(StoreIconImage, StoreIconRect)


def draw_window(player_):
    draw_general_win(player_)

    if player_.in_store_:
        store.draw(Screen)

    if player_.money_error_time:
        player_.money_error_time -= 1
        Draw.print_text("You haven't enough money",
                        Screen, Global.FontTitle)

    pg.display.update()


while player_.running:
    clock.tick(Global.FPS)

    Uc.check_events(player_)
    Uc.update(player_)
    draw_window(player_)

pg.quit()
sys.exit()
