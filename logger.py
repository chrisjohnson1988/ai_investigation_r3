class Logging:

    def __init__(self, level='INFO'):
        self.level = level

    def log(self, message, level='INFO'):
        if self._should_log(level):
            print(f'[{level}] {message}')

    def _should_log(self, level):
        levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        return levels.index(level) >= levels.index(self.level)