import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，设置rect属性
        self.image1 = pygame.image.load('../images/ship.bmp')
        self.image = pygame.transform.scale(self.image1, (35, 35))  # 改变图片大小
        self.rect = self.image.get_rect()

        # 每个外星人最初在屏幕左上角
        self.rect.y = self.rect.height
        self.rect.x = self.rect.width

        self.rect.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果位于屏幕边缘，返回Ture"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左，向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
