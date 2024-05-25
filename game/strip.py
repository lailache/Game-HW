from pathlib import Path
import pygame
import random

CURRENT_FOLDER = Path(__file__).parent

STRIP_WIDTH = 128
STRIP_HEIGHT = 72


class Strip(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.scene = pygame.display.get_surface().get_rect()

        self.image = pygame.Surface((STRIP_WIDTH, STRIP_HEIGHT))
        self.color = self.get_random_color()
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.y_speed = 8

        # Store the trail
        self.trail = []

    @staticmethod
    def get_random_color():
        line_color = [random.randint(0, 255) for _ in range(3)]
        return line_color

    def update(self):
        self.rect.y += self.y_speed

        # Prevent the strip from going off the screen
        if self.rect.bottom > self.scene.bottom:
            self.rect.y = self.scene.top
            self.color = self.get_random_color()
        # Add the current position to the trail
        self.trail.append((self.rect.topleft, self.color))

        # Limit the trail length
        if len(self.trail) > 500:
            self.trail.pop(0)

    def change_color(self):
        self.color = self.get_random_color()
        self.image.fill(self.color)



