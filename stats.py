class Stats():
    """статистика"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        self.score = 0
        with open('high_score.txt', 'r') as f:
            score = f.readline()
            if score:
                self.high_score = int(score)
            else:
                self.high_score = 0

    def reset_stats(self):
        """изменяющяяся статистика"""
        self.guns_left = 2

