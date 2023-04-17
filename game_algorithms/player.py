class Player:
    def __init__(self, nr):
        self.nr = nr
        self.strategies = {}
        self.opponent: Player = None

    def add_strategy(self, name, strategy):
        self.strategies[name] = strategy
