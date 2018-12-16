import pygame

class Point:
    color = (0, 0, 0)
    selected_color = (0, 255, 100)
    radius = 8

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, selected):
        color = None
        if selected:
            color = self.selected_color
        else:
            color = self.color
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
