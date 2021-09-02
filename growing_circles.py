import sys
from time import sleep
from random import randint
import pygame

WHITE = (255, 255, 255, 255)

class Circle:
    """Hold data an methods for drawing a circle
    """

    def __init__(self, surface_size: tuple[int, int]):
        x = randint(0, surface_size[0]-1)
        y = randint(0, surface_size[1]-1)

        # Max radius is reached when the circle touches all corners
        corners = [(0, 0),
                   (0, surface_size[1]),
                   (surface_size[0], surface_size[1]),
                   (surface_size[0], 0)]
        distances = [int(((corn[0]-x)**2 + (corn[1]-y)**2)**0.5)
                     for corn in corners]
        self.max_radius = max(distances)

        self.pos = (x, y)
        self.radius = 1
        self.color = random_color()

    def draw(self, surface: pygame.Surface) -> None:
        # pygame.draw will not draw alpha
        # Workaround: using a helper surface with alpha and blitting it
        helper_surface = pygame.Surface((self.radius*2, self.radius*2), flags=pygame.SRCALPHA)
        helper_surface.set_alpha(127)
        pygame.draw.circle(helper_surface, self.color, (self.radius, self.radius), self.radius)
        surface.blit(helper_surface, (self.pos[0]-self.radius, self.pos[1]-self.radius))


class GrowingCircles:
    """Growing Circles on a pygame Screen
    """

    def __init__(self, resolution: tuple, num_circles: int = 5):
        pygame.init()
        self.resolution = resolution
        self.num_circles = num_circles
        flags = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(resolution, flags, vsync=1)
        self.circles = []

        self._make_circles()

    def _make_circles(self) -> None:
        missing = self.num_circles - len(self.circles)
        for _ in range(missing):
            self.circles.append(Circle((self.resolution)))

    def _update(self) -> None:
        self.circles = list(filter(
            lambda circ: True if circ.radius <= circ.max_radius else False,
            self.circles))

        # Are there enough circles?
        if len(self.circles) < self.num_circles:
            self._make_circles()

        for circle in self.circles:
            circle.radius += 2

    def _draw(self) -> None:
        for circle in self.circles:
            circle.draw(self.screen)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update()
            self.screen.fill(WHITE)
            self._draw()
            pygame.display.flip()


def random_color() -> tuple:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def main():
    size = (1920, 1080)
    app = GrowingCircles(size)
    app.run()


if __name__ == "__main__":
    main()
