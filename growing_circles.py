import sys
from time import sleep
from random import randint
import pygame

WHITE = (255, 255, 255)

class Circle:
    """Hold data an methods for drawing a circle
    """

    def __init__(self, pos: tuple, radius: int, color: tuple):
        self.pos = pos
        self.radius = radius
        self.color = color

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


class GrowingCircles:
    """Growing Circles on a pygame Screen
    """

    def __init__(self, resolution: tuple, num_circles: int = 5):
        pygame.init()
        self.size = resolution
        self.num_circles = num_circles
        self.screen = pygame.display.set_mode(resolution, vsync=1)
        self.circles = []

        self._make_circles()

    def _make_circles(self) -> None:
        for _ in range(self.num_circles):
            x = randint(0, self.size[0]-1)
            y = randint(0, self.size[1]-1)
            radius = 1
            color = random_color()

            self.circles.append(Circle((x, y), radius, color))

    def _update(self) -> None:
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
            sleep(0.1)


def random_color() -> tuple:
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def main():
    size = (1280, 720)
    app = GrowingCircles(size)
    app.run()


if __name__ == "__main__":
    main()
