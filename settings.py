import pygame

class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_flags = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF

        self.num_circles = 5
        self.initial_radius = 1
        self.radius_growth = 2
