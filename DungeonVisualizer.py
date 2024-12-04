import pygame
pygame.init()

class DungeonVisualizer:
    def __init__(self, window):
        self.window = window
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
