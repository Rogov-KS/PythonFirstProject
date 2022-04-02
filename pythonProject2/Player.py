import pygame


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
