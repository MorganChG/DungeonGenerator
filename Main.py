import math
import random
import pygame

class DungeonVisualizer:
    def __init__(self, window):
        self.window = window

    def draw(self, rooms):
        for room in rooms:
            self.draw_room(self.get_corners(room.get_position(), room.get_width(), room.get_height()))
            self.draw_door(room)

    def draw_room(self, corners):
        for i in range(0, len(corners) // 2):
            pygame.draw.line(self.window, (240, 240, 240), corners[0 - i], corners[1 + i],2)  # Draws from TL to TR and BL to BR
            pygame.draw.line(self.window, (240, 240, 240), corners[0 + i], corners[2 + i],2)  # Draws from TL to BL and TR to BR

    def draw_door(self, room):
        for door in room.get_doors():
            pygame.draw.circle(self.window, (200, 40, 40), door.get_position(), 3)

    @staticmethod
    def get_corners(room_pos, room_width, room_height):
        x,y = room_pos

        return [(x - room_width // 2, y - room_height // 2),  #Top Left Corner
                (x + room_width//2, y - room_height // 2),    #Top Right Corner
                (x - room_width//2, y + room_height // 2),    #Bottom Left Corner
                (x + room_width//2, y + room_height // 2)]    #Bottom Right Corner


class DungeonGenerator:
    def __init__(self, window, number_of_rooms=10):
        self.window = window
        self.number_of_rooms = number_of_rooms

    @staticmethod
    def get_next_room_height(door, height):
        height_max = abs(door[1])
        if door[1] > 300: height_max = 600 - height_max
        return random.randint(height - height_max, height_max)

    @staticmethod
    def get_next_room_width(door, width):
        width_max = abs(door[0])
        if door[0] > 300: width_max = 600 - width_max
        return random.randint(width - width_max, width_max)

    @staticmethod
    def offset_next_room_x(room, door, width):
        x_difference = door[0] - room.x
        print(x_difference)
        if x_difference != 0:
            if x_difference < 0: return door[0] - width // 2
            else: return door[0] + width // 2
        return door[0]

    @staticmethod
    def offset_next_room_y(room, door, height):
        y_difference = door[1] - room.y
        if y_difference != 0:
            if y_difference < 0: return door[1] - height // 2
            else: return door[1] + height // 2
        return door[1]

    def generate(self, rooms):
        while len(rooms) < self.number_of_rooms:
            pass




class Door:
    def __init__(self, x : int, y : int, connected : bool = False, other = None):
        self.x = x
        self.y = y
        self.connected = connected
        self.other = other

    def set_connected(self, boolean : bool):
        self.connected = boolean

    def set_connected_door(self, door):
        self.other = door

    def get_position(self):
        return self.x,self.y

    def get_connected_door(self):
        return self.other

    def is_connected(self):
        return self.connected

class Room:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.doors = self.set_doors()
        self.remove_doors()

    def pick_door(self):
        door = random.choice(self.doors)
        self.remove_door(door)
        return door

    def remove_doors(self):
        for i in range(random.randint(0,len(self.doors)-1)):
            index = random.randint(0,len(self.doors)-1)
            self.doors.pop(index)

    def remove_door(self, door):
        self.doors.remove(door)

    def get_position(self):
        return self.x, self.y

    def get_number_of_doors(self):
        return len(self.doors)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_doors(self):
        return self.doors

    def set_doors(self):
        return [Door(self.x - self.width // 2, self.y),     #Left Door
                Door(self.x + self.width // 2, self.y),     #Right Door
                Door(self.x, self.y - self.height // 2),    #Top Door
                Door(self.x, self.y + self.height // 2)]    #Bottom Door

    @staticmethod
    def distance(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


class Main:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600), pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.running = True
        self.visualizer = DungeonVisualizer(self.window)
        self.generator = DungeonGenerator(self.window)

        self.starting_room = Room(self.window, 300, 300, 50, 50)
        self.rooms = [self.starting_room]


    def update(self):
        while self.running:
            for event in pygame.event.get():
                self.running = not self.is_exit_button_pressed(event)
            self.update_background()
            self.visualizer.draw(self.rooms)
            self.update_pygame()
            self.update_frames()

    def update_frames(self):
        self.clock.tick(10)

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