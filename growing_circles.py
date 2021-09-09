"""
This module contains logic for growing circles
"""
import sys
from random import randint

import pyglet

from settings import Settings
settings = Settings()

WHITE = (255, 255, 255, 255)

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window(width=settings.screen_width,
                              height=settings.screen_height)
window.config.alpha_size = 8

class Circle:
    """
    Holds data an methods for drawing a circle
    """

    def __init__(self, surface_size: tuple[int, int]):
        self.x = randint(0, surface_size[0]-1)
        self.y = randint(0, surface_size[1]-1)

        # Max radius is reached when the circle touches all corners
        corners = [(0, 0),
                   (0, surface_size[1]),
                   (surface_size[0], surface_size[1]),
                   (surface_size[0], 0)]
        distances = [int(((corn[0]-self.x)**2 + (corn[1]-self.y)**2)**0.5)
                     for corn in corners]
        self.max_radius = max(distances)

        self.radius = settings.initial_radius
        self.color = random_color()

    def draw(self) -> None:
        """
        Draws a single circle
        """
        circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.color)
        circle.opacity = 128
        circle.draw()


class GrowingCircles:
    """
    Growing Circles on a pyglet Screen
    """

    def __init__(self, resolution: tuple, num_circles: int = 5):
        self.resolution = resolution
        self.num_circles = num_circles
        self.circles = []

        self._make_circles()

    def _make_circles(self) -> None:
        missing = self.num_circles - len(self.circles)
        for _ in range(missing):
            self.circles.append(Circle((self.resolution)))

    def _update(self) -> None:
        # Are there circles that are fully grown?
        self.circles = list(filter(
            lambda circ: True if circ.radius <= circ.max_radius else False,
            self.circles))

        # Are there enough circles?
        if len(self.circles) < self.num_circles:
            self._make_circles()

        for circle in self.circles:
            circle.radius += settings.radius_growth

    def draw(self) -> None:
        for circle in self.circles:
            circle.draw()


def random_color() -> tuple:
    """
    Generates a random color without alpha

    Returns:
        tuple: tuple representing (R, G, B)
    """
    return (randint(0, 255), randint(0, 255), randint(0, 255))


@window.event
def on_draw():
    window.clear()
    gc._update()
    gc.draw()

size = (settings.screen_width, settings.screen_height)
gc = GrowingCircles(size, settings.num_circles)

def main():
    """
    Run the application if the module itself is run
    """
    pyglet.app.run()


if __name__ == "__main__":
    main()
