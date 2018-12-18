import pygame
import random
from objects.Point import Point, ControlPoint
from objects.BezierCurve import BezierCurve
from objects.ConstructCurve import ConstructCurve

# Constants
MOUSEBUTTONLEFT = 1
MOUSEBUTTONMIDDLE = 2
MOUSEBUTTONRIGHT = 3

# Variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
dimension = (SCREEN_WIDTH, SCREEN_HEIGHT)
background_color = (255, 255, 255)
control_points_line_color = (150, 150, 150)
nr_of_points = 6
bezier_curve_steps = 200

def main():
    # Init screen
    pygame.init()

    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption('Bezier curves')

    points = get_random_points(nr_of_points)
    selected_point = None
    selected_curve_point_t = None
    bezier_curve = BezierCurve(points, bezier_curve_steps)
    construct_curve = None

    running = True;

    while running:
        # Events
        for event in pygame.event.get():
            # System events
            if event.type == pygame.QUIT:
                running = False

            # Key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    points = get_random_points(nr_of_points)
                    bezier_curve = BezierCurve(points, bezier_curve_steps)
                    construct_curve = None
                    selected_curve_point_t = None

            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSEBUTTONLEFT:
                    # Get selected point
                    x, y = pygame.mouse.get_pos()
                    selected_point = get_selected_point(points, x, y)
                    if selected_point == None:
                        ((px, py), t) = bezier_curve.get_point_on_curve(x, y)
                        selected_curve_point_t = t
                        construct_curve = ConstructCurve(points, t)

            if event.type == pygame.MOUSEBUTTONUP:
                if not selected_point == None:
                    selected_point = None

        # Logic
        if not selected_point == None:
            selected_point.set_position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        # Render
        screen.fill(background_color)

        for point in points:
            point.draw(screen, point == selected_point)
        for i in range(len(points) - 1):
            start = (points[i].x, points[i].y)
            end = (points[i + 1].x, points[i + 1].y)
            pygame.draw.line(screen, control_points_line_color, start, end)
        if not selected_curve_point_t == None:
            x, y = bezier_curve.get_point(selected_curve_point_t)
            Point(x, y).draw(screen)
        if not construct_curve == None:
            construct_curve.draw(screen)

        bezier_curve.draw(screen)

        pygame.display.flip()

def get_selected_point(points, x, y):
    for point in points:
        if point.x - point.radius < x and point.x + point.radius > x:
            if point.y - point.radius < y and point.y + point.radius > y:
                return point
    return None

def get_random_points(n):
    points = []
    for i in range(n):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        points.append(ControlPoint(x, y))
    return points

if __name__ == '__main__':
    main()
