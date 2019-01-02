import pygame
import random
from objects.Point import Point

class ConstructCurve:
    def __init__(self, control_points, t):
        self.control_points = control_points
        self.t = t

    def draw(self, screen):
        points = self.control_points
        colors = self.get_colors(len(points))
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
                pygame.draw.line(screen, colors[n], p1.as_list(), p2.as_list(), 2)
            points = new_points
            new_points = []

    def get_colors(self, n):
        colors = []
        random.seed(n)
        r = int(random.random() * 256)
        g = int(random.random() * 256)
        b = int(random.random() * 256)
        step = 256 / n
        for i in range(n):
            r += step
            g += step
            b += step
            r = int(r) % 256
            g = int(g) % 256
            b = int(b) % 256
            colors.append((r,g,b))
        return colors

        return (r, g, b)
