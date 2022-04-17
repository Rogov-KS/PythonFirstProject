def is_in_store(x: int, y: int) -> bool:
    return 1150 >= x >= 1000 and 765 >= y >= 600


def is_1_item(x: int, y: int) -> bool:
    return 1200 >= x >= 1100 and 100 <= y <= 200


def is_2_item(x: int, y: int) -> bool:
    return 1200 >= x >= 1100 and 220 <= y <= 300


def is_3_item(x: int, y: int) -> bool:
    return 1200 >= x >= 1100 and 310 <= y <= 400


def is_4_item(x: int, y: int) -> bool:
    return 1200 >= x >= 1100 and 410 <= y <= 500


def is_5_item(x: int, y: int) -> bool:
    return 1200 >= x >= 1100 and 520 <= y <= 610
