import math
import random
import pygame

class DungeonVisualizer:
    def __init__(self, window):
        self.window = window
        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 10)

    def draw(self, rooms, edges):
        for room in rooms:
            #self.draw_index(room, rooms)
            self.draw_room(self.get_corners(room.get_position(), room.get_width(), room.get_height()))
            #self.draw_door(room)
        for i in range(len(edges)):
            pygame.draw.line(self.window, (200,200,200), edges[i][0].get_position(), edges[i][1].get_position(), 2)

    def draw_index(self, room, rooms):
        text = self.font.render(str(rooms.index(room)), True, (255, 255, 255))
        self.window.blit(text, room.get_position())

    def draw_room(self, corners):
        for i in range(0, len(corners) // 2):
            pygame.draw.line(self.window, (240, 240, 240), corners[0 - i], corners[1 + i],2)  # Draws from TL to TR and BL to BR
            pygame.draw.line(self.window, (240, 240, 240), corners[0 + i], corners[2 + i],2)  # Draws from TL to BL and TR to BR

    def draw_door(self, room):
        for door in room.get_doors():
            pygame.draw.circle(self.window, (200, 40, 40), door.get_position(), 2)

    @staticmethod
    def get_corners(room_pos, room_width, room_height):
        x,y = room_pos

        return [(x - room_width // 2, y - room_height // 2),  #Top Left Corner
                (x + room_width//2, y - room_height // 2),    #Top Right Corner
                (x - room_width//2, y + room_height // 2),    #Bottom Left Corner
                (x + room_width//2, y + room_height // 2)]    #Bottom Right Corner
class DungeonGenerator:
    def __init__(self, number_of_rooms, size):
        self.number_of_rooms = number_of_rooms
        self.check_number_of_rooms(size)

    def check_number_of_rooms(self, size):
        if not self.is_proper_number_of_rooms(size):
            proper_size = (600 // (size * 2)) ** 2
            raise Exception(f"too many rooms for room_size try : {proper_size}")

    def is_proper_number_of_rooms(self, size):
        return self.number_of_rooms <= (600 // (size * 2)) ** 2

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
    def offset_x(room_position, door_position, distance):
        x_difference = door_position[0] - room_position[0]
        if x_difference != 0:
            if x_difference < 0: return door_position[0] - distance // 2
            else: return door_position[0] + distance // 2
        return door_position[0]

    @staticmethod
    def offset_y(room_position, door_position, distance):
        y_difference = door_position[1] - room_position[1]
        if y_difference != 0:
            if y_difference < 0: return door_position[1] - distance // 2
            else: return door_position[1] + distance // 2
        return door_position[1]

    @staticmethod
    def is_not_already_a_room(offset_x, offset_y, rooms):
        for room in rooms:
            if (offset_x, offset_y) == room.get_position():
                return False
        return True


    @staticmethod
    def is_within_bounds(offset_x, offset_y):
        return 0 < offset_x < 600 and 0 < offset_y < 600

    def generate(self, rooms, path):
        index = 0
        while len(rooms) < self.number_of_rooms:
            if index >= 0:
                if len(rooms[index].get_doors()) > 0:
                    door = rooms[index].pick_door()
                    offset_x = self.offset_x(rooms[index].get_position(), door.get_position(), rooms[index].get_width() * 2)
                    offset_y = self.offset_y(rooms[index].get_position(), door.get_position(), rooms[index].get_height() * 2)
                    if self.is_within_bounds(offset_x, offset_y):
                        new_door = Door(offset_x,offset_y)
                        room_x = self.offset_x(rooms[index].get_position(), new_door.get_position(),rooms[index].get_width())
                        room_y = self.offset_y(rooms[index].get_position(), new_door.get_position(), rooms[index].get_height())
                        if self.is_not_already_a_room(room_x, room_y, rooms):
                            new_room = Room(room_x,room_y,rooms[index].get_width(), rooms[index].get_height())
                            path.add(door, new_door)
                            new_room.remove_door_from_position(new_door.get_position())
                            rooms.append(new_room)
                            index += 1
                else:
                    index -= 1
            else:
                index = len(rooms) - 1

class Path:
    def __init__(self):
        self.path = []

    def add(self, door1, door2):
        self.path.append((door1, door2))

    def get_path(self):
        return self.path

    def clear(self):
        self.path = []


class Door:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x,self.y


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.doors = self.set_doors()
        #print(self.doors)

    def pick_door(self):
        #print(self.doors)
        door = random.choice(self.doors)
        self.remove_door(door)
        return door

    def remove_doors(self):
        for i in range(random.randint(1,len(self.doors)-1)):
            index = random.randint(0,len(self.doors)-1)
            self.doors.pop(index)

    def remove_door(self, door):
        self.doors.remove(door)

    def remove_door_from_position(self, door_position):
        for door in self.doors:
            if door.get_position() == door_position:
                self.remove_door(door)


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
        self.room_size = 40

        self.path = Path()
        self.visualizer = DungeonVisualizer(self.window)
        self.generator = DungeonGenerator(49, self.room_size)
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