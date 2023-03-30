class GameStats:
    """跟踪游戏的统计数据"""
    def __init__(self,ai_settings):
        """初始化统计数据"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏开关
        self.game_active = True

    def reset_stats(self):
        """初始化游戏可能统计数据"""
        self.ships_left = self.ai_settings.ship_limit
