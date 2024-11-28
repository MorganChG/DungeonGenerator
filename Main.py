import pygame
class Main:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600), pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        while self.running:
            for event in pygame.event.get():
                self.running = not self.is_exit_button_pressed(event)

    @staticmethod
    def is_exit_button_pressed(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return True
        return False