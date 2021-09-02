import sys
from time import sleep
from random import randint
import pygame

WHITE = (255, 255, 255)

class Circle:
    """Hold data an methods for drawing a circle
    """

    def __init__(self, surface_size: tuple[int, int]):
        x = randint(0, surface_size[0]-1)
        y = randint(0, surface_size[1]-1)
        
        # Max radius is reached when the radius reaches the left and the right
        # side of the screen
        self.max_radius = max(x, surface_size[0] - x)

        self.pos = (x, y)
        self.radius = 1
        self.color = random_color()

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


class GrowingCircles:
    """Growing Circles on a pygame Screen
    """

    def __init__(self, resolution: tuple, num_circles: int = 5):
        pygame.init()
        self.resolution = resolution
        self.num_circles = num_circles
        self.screen = pygame.display.set_mode(resolution, vsync=1)
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
            circle.radius += 1

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
            sleep(0.01)


def random_color() -> tuple:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def main():
    size = (1280, 720)
    app = GrowingCircles(size)
    app.run()


if __name__ == "__main__":
    main()
