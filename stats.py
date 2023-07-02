class Stats():
    """статистика"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """изменяющяяся статистика"""
        self.guns_left = 2
        self.score = 0

