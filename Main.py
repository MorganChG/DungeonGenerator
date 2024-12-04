import math
import random
import pygame

from DungeonVisualizer import DungeonVisualizer
from DungeonGenerator import DungeonGenerator
from Room import Room
from Path import Path

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600), pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.running = True
        self.room_size = 10

        self.path = Path()
        self.visualizer = DungeonVisualizer(self.window)
        self.generator = DungeonGenerator(200, self.room_size)
        self.starting_room = Room(300, 300, self.room_size, self.room_size)

        self.rooms = [self.starting_room]

        self.generator.generate(self.rooms, self.path)

    def update(self):
        while self.running:
            for event in pygame.event.get():
                self.running = not self.is_exit_button_pressed(event)
            self.update_background()
            self.visualizer.draw(self.rooms, self.path.get_path())
            self.update_pygame()
            #self.update_frames()

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