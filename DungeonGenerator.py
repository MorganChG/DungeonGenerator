import random

from Door import Door
from Room import Room

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

    def generate(self, rooms, path):
        index = 0
        while self.has_enough_rooms(rooms):
            if index >= 0:

                room_position = self.get_room_position(index, rooms)

                if self.does_room_have_doors(index, rooms):

                    door = self.get_door(index, rooms)

                    offset_x = self.offset_x(room_position, door.get_position(), rooms[index].get_width() * 2)
                    offset_y = self.offset_y(room_position, door.get_position(), rooms[index].get_height() * 2)

                    if self.is_within_bounds(offset_x, offset_y):

                        new_door = Door(offset_x, offset_y)

                        room_x = self.offset_x(room_position, new_door.get_position(), rooms[index].get_width())
                        room_y = self.offset_y(room_position, new_door.get_position(), rooms[index].get_height())

                        if self.is_not_already_a_room(room_x, room_y, rooms):
                            self.add_room_to_rooms(door, index, new_door, path, room_x, room_y, rooms)
                            index += 1
                else:
                    index -= 1
            else:
                index = len(rooms) - 1

    def has_enough_rooms(self, rooms):
        return len(rooms) < self.number_of_rooms

    def add_room_to_rooms(self, door, index, new_door, path, room_x, room_y, rooms):
        new_room = self.create_room(index, room_x, room_y, rooms)
        self.update_path(door, new_door, path)
        self.remove_door(new_door, new_room)
        self.add_room(new_room, rooms)

    @staticmethod
    def update_path(door, new_door, path):
        path.add(door, new_door)

    @staticmethod
    def add_room(new_room, rooms):
        rooms.append(new_room)

    @staticmethod
    def create_room(index, room_x, room_y, rooms):
        return Room(room_x, room_y, rooms[index].get_width(), rooms[index].get_height())

    @staticmethod
    def remove_door(new_door, new_room):
        new_room.remove_door_from_position(new_door.get_position())

    @staticmethod
    def get_door(index, rooms):
        return rooms[index].pick_door()

    @staticmethod
    def get_room_position(index, rooms):
        return rooms[index].get_position()

    @staticmethod
    def does_room_have_doors(index, rooms):
        return len(rooms[index].get_doors()) > 0

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
            if x_difference < 0:
                return door_position[0] - distance // 2
            else:
                return door_position[0] + distance // 2
        return door_position[0]

    @staticmethod
    def offset_y(room_position, door_position, distance):
        y_difference = door_position[1] - room_position[1]
        if y_difference != 0:
            if y_difference < 0:
                return door_position[1] - distance // 2
            else:
                return door_position[1] + distance // 2
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