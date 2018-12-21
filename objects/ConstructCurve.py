import pygame
import math
from objects.Point import Point

class ConstructCurve:
    def __init__(self, control_points, t):
        self.control_points = control_points
        self.t = t

    def draw(self, screen):
        points = self.control_points
        new_points = []
        while len(points) > 2:
            n = len(points) - 1
            # Get points
            for i in range(n):
                new_points.append(Point.interpolate(points[i], points[i + 1], self.t))
            # Draw points
            for i in range(n - 1):
                p1 = new_points[i]
                p2 = new_points[i + 1]
                color = self.get_color(n)
                pygame.draw.line(screen, color, p1.as_list(), p2.as_list())
            points = new_points
            new_points = []

    def get_color(self, n):
        r = abs(math.sin(n)) * 150 + 100
        g = abs(math.sin(n)) * 50 + 50
        b = abs(math.sin(n)) * 50 + 100

        return (r, g, b)
