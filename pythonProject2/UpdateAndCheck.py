import pygame as pg

def CheckEvents(player_):
    events_ = pg.event.get()
    for event in events_:
        if event.type == pg.QUIT:
            player_.running = False
        if event.type ==  pg.MOUSEBUTTONDOWN:
            if event.button == 1: ## работает
                player_.click_qution += 10
                player_.score_ += 1 * player_.click_qution
                player_.auto_clicks_ += 10
            elif event.button == 3:
                (x, y) = pg.mouse.get_pos()
                if x >= 1000 and y >= 600:
                    player_.in_store_ = player_.in_store_ ^ 1
                if player_.in_store_ and x >= 1150 and y >= 100 and y <= 200:
                    if player_.score_ >= 2000:
                        player_.score_ -= 2000
                        player_.AddAutoClicks(100)
                    else:
                        player_.MoneyErrortime = 30

    Keys = pg.key.get_pressed()
    if Keys[pg.K_SPACE] or Keys[pg.K_LEFT] or Keys[pg.K_RIGHT]:
        player_.score_ += 1 * player_.click_qution
        player_.score_ += 1 * player_.click_qution


def Update(player_):
    player_.score_ += (max(1, player_.auto_clicks_ // 30))
    return
