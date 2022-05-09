import GlobalVariable as Global


def make_score_title(score, font_title):
    score_title = font_title.render(
        f"Score: {score}", True, Global.RED)
    score_rect = score_title.get_rect()
    score_rect.left = 75
    return score_title, score_rect


def make_auto_click_title(auto_clicks, font_title):
    auto_click_title = font_title.render(
        f"AutoClick: {auto_clicks} / sec", True, Global.RED)
    auto_rect = auto_click_title.get_rect()
    auto_rect.topleft = (75, 50)
    return auto_click_title, auto_rect


def make_bonus(bonus, image_rect, title):
    bonus = title.render(bonus, True, Global.RED)
    bonus_rect = (image_rect[0] - 50, image_rect[1] + 70)
    return bonus, bonus_rect


def make_price(price, image_rect, title):
    price = title.render(
        f"Coast: {price}", True, Global.RED)
    price_rect = (image_rect[0] - 50, image_rect[1] - 10)
    return price, price_rect


def print_text(text, screen, title):
    text = title.render(text, True, Global.RED)
    text_rect = text.get_rect()
    text_rect.center = (Global.WIDTH // 2, 100)
    screen.blit(text, text_rect)
