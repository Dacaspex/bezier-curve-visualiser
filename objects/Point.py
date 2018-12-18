import pygame

class Point:
    def __init__(self, x, y, color = (0, 0, 0), radius = 8):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def as_list(self):
        return (self.x, self.y)

    @staticmethod
    def interpolate(p1, p2, alpha):
        x = (1 - alpha) * p1.x + alpha * p2.x
        y = (1 - alpha) * p1.y + alpha * p2.y
        return Point(x, y)

class ControlPoint(Point):
    selected_color = (0, 255, 100)

    def __init__(self, x, y):
        Point.__init__(self, x, y)

    def draw(self, screen, selected):
        color = None
        if selected:
            color = self.selected_color
        else:
            color = self.color
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
