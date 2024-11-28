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
            self.update_background()
            self.update_pygame()
            self.update_frames()

    def update_frames(self):
        self.clock.tick(60)

    def update_background(self):
        self.window.fill((40, 40, 40))

    @staticmethod
    def update_pygame():
        pygame.display.update()

    @staticmethod
    def is_exit_button_pressed(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return True
        return False

if __name__ == '__main__':
    Main().update()