import random
import math

from Door import Door

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.doors = self.set_doors()

    def pick_door(self):
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