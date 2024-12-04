class Path:
    def __init__(self):
        self.path = []

    def add(self, door1, door2):
        self.path.append((door1, door2))

    def get_path(self):
        return self.path

    def clear(self):
        self.path = []
