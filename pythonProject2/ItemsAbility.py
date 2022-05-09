def saber_ability(player_):
    if player_.score_ >= 2000:
        player_.score_ -= 2000
        player_.add_auto_clicks(100)
    else:
        player_.money_error_time = 30


def space_ship_ability(player_):
    if player_.score_ >= 3000:
        player_.score_ -= 3000
        player_.click_quotient += 100
    else:
        player_.money_error_time = 30


def legendary_ship_ability(player_):
    if player_.score_ >= 5000:
        player_.score_ -= 5000
        pass
    else:
        player_.money_error_time = 30
