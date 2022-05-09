import pygame as pg
import ItemsAbility as Ability
import Is_in_store as IsIn


def check_events(player_):
    events_ = pg.event.get()
    for event in events_:
        if event.type == pg.QUIT:
            player_.running = False

        if event.type == pg.MOUSEBUTTONDOWN:

            if event.button == 1:
                player_.click_quotient += 10
                player_.score_ += player_.click_quotient

            elif event.button == 3:
                (x, y) = pg.mouse.get_pos()

                if IsIn.is_in_store(x, y):
                    player_.in_store_ = player_.in_store_ ^ 1

                if player_.in_store_ and IsIn.is_1_item(x, y):
                    Ability.saber_ability(player_)

                if player_.in_store_ and IsIn.is_2_item(x, y):
                    Ability.saber_ability(player_)

                if player_.in_store_ and IsIn.is_3_item(x, y):
                    Ability.space_ship_ability(player_)

                if player_.in_store_ and IsIn.is_4_item(x, y):
                    Ability.space_ship_ability(player_)

                if player_.in_store_ and IsIn.is_5_item(x, y):
                    Ability.legendary_ship_ability(player_)

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        player_.score_ += player_.click_quotient


def update(player_):
    player_.score_ += player_.auto_clicks_
