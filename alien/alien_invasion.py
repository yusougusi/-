import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建统计实例
    stats = GameStats(ai_settings)
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个储存子弹的编组
    bullets = Group()
    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # 监视键盘和鼠标事件

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 更新屏幕上的图像，并切换到新屏幕


run_game()
