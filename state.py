class AppState:
    def __init__(self):
        self.running = False
        self.speed = 300  # ms
        self.algorithm = None
        self.iterator = None
        self.steps = 0
