import random
import pygame

class Room:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.corners = self.get_corners()
        self.doors = self.get_doors()

    def draw(self):
        for i in range(0, len(self.corners) // 2):
            pygame.draw.line(self.window, (240,240,240), self.corners[0 - i], self.corners[1 + i], 2)   #Draws from TL to TR and BL to BR
            pygame.draw.line(self.window, (240,240,240), self.corners[0 + i], self.corners[2 + i], 2)   #Draws from TL to BL and TR to BR

        for door in self.doors:
            pygame.draw.circle(self.window, (200,40,40), door, 3)



    def get_corners(self):
        return [(self.x - self.width // 2, self.y - self.height // 2),  #Top Left Corner
                (self.x + self.width//2, self.y - self.height // 2),    #Top Right Corner
                (self.x - self.width//2, self.y + self.height // 2),    #Bottom Left Corner
                (self.x + self.width//2, self.y + self.height // 2)]    #Bottom Right Corner

    def get_doors(self):
        return [(self.x - self.width // 2, self.y),     #Left Door
                (self.x + self.width // 2, self.y),     #Right Door
                (self.x, self.y - self.height // 2),    #Top Door
                (self.x, self.y + self.height // 2)]    #Bottom Door


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
            Room(self.window, random.randint(100, 500),random.randint(100, 500), random.randint(50, 200), random.randint(50, 200)).draw()
            self.update_pygame()
            self.update_frames()

    def update_frames(self):
        self.clock.tick(1)

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