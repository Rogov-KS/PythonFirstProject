import pygame as pg
from GlobalVariable import *


def MakeScoreTitle(score, fontTitle):
    ScoreTitle = fontTitle.render(f"Score: {score}", True, RED)
    ScoreRect = ScoreTitle.get_rect()
    ScoreRect.left = 75
    return (ScoreTitle, ScoreRect)

def MakeAutoClickTitle(autoclicks, fontTitle):
    AutoClickTitle = fontTitle.render(f"AutoClick: {autoclicks} / sec", True, RED)
    AutoRect = AutoClickTitle.get_rect()
    AutoRect.topleft = (75, 50)
    return (AutoClickTitle, AutoRect)

def MakeBonus(bonus, ImageRect, Title):
    Bonus = Title.render(bonus, True, RED)
    BonusRect = (ImageRect[0] - 50, ImageRect[1] + 70)
    return (Bonus, BonusRect)

def MakePrice(price, ImageRect, Title):
    Price = Title.render(f"Coast: {price}", True, RED)
    PriceRect = (ImageRect[0] - 50, ImageRect[1] - 10)
    return (Price, PriceRect)

def print_text(str, Screen, Title):
    Text = Title.render(str, True, RED)
    TextRect = Text.get_rect()
    TextRect.center = (WIDTH // 2, 100)
    Screen.blit(Text, TextRect)
