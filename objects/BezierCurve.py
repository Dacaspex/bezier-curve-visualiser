import pygame
import math
from objects.Point import Point

class BezierCurve:
    color = (0, 100, 255)
    normal_color = (127, 175, 25)
    width = 2
    normal_width = 1
    normal_step = 10

    def __init__(self, control_points, steps):
        self.control_points = control_points
        self.steps = steps

    def draw(self, screen):
        step = 1 / self.steps
        points = []
        normals = []

        # Create points
        for i in range(self.steps):
            t = step * i
            points.append(self.get_point(t))
            # Calculate normal to line
            x, y = self.get_derivate(t)
            length = math.sqrt(x**2 + y**2) / 20
            normals.append((-y / length, x / length))

        # Draw line
        for i in range(self.steps - 1):
            pygame.draw.line(screen, self.color, points[i], points[i + 1], self.width)
            if i % self.normal_step == 0:
                normal_start = (points[i][0] - normals[i][0], points[i][1] - normals[i][1])
                normal_end = (points[i][0] + normals[i][0], points[i][1] + normals[i][1])
                pygame.draw.line(screen, self.normal_color, normal_start, normal_end, self.normal_width)

    def get_point(self, t):
        # B(t) = sum_{i = 0}^{n} ( (n above i) * (1 - t)^{n - i} * t^i * P )
        x = 0;
        y = 0;
        n = len(self.control_points) - 1
        for i in range(n + 1):
            x += self.get_polynomial(n, i, t) * self.control_points[i].x
            y += self.get_polynomial(n, i, t) * self.control_points[i].y
        return (x, y)

    def get_derivate(self, t):
        x = 0;
        y = 0;
        n = len(self.control_points) - 1
        for i in range(n):
            x += self.get_polynomial(n - 1, i, t) * (self.control_points[i + 1].x - self.control_points[i].x)
            y += self.get_polynomial(n - 1, i, t) * (self.control_points[i + 1].y - self.control_points[i].y)
        return (x * n, y * n)

    def get_point_on_curve(self, x, y):
        found_t = 0
        min_error = 1000 # infinite
        step = 1 / self.steps
        for i in range(self.steps):
            t = step * i
            px, py = self.get_point(t)
            error = math.sqrt((px - x)**2 + (py - y)**2)
            if error < min_error:
                min_error = error
                found_t = t

        return self.get_point(found_t)

    def get_binom(self, n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    def get_polynomial(self, n, i, t):
        return self.get_binom(n, i) * (1 - t)**(n - i) * t**i
