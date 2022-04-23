
class Switch:
    """
    Switch class for panel buttons with decorator pattern (I KNOW I AM GOING CRAZY WITH DECORATOR PATTERNS IN THIS PROJECT).
    """
    def __init__(self, gameParam, key, switchTo, decorator = None):
        self.decorator = decorator
        self.gameParam = gameParam
        self.key = key
        self.switchTo = switchTo
    def apply(self):
        if self.decorator != None:
            self.decorator.apply()
        self.gameParam[self.key] = self.switchTo