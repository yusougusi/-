import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图像并获取外接矩形
        self.image = pygame.image.load('../images/ship.bmp')
        self.image1 = pygame.transform.scale(self.image, (50, 50))  # 改变图片大小
        self.rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #  在飞船属性center中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        #  更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #  根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image1, self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.center = self.screen_rect.centerx
