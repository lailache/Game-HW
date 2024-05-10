from pathlib import Path
import pygame
import random

CURRENT_FOLDER = Path(__file__).parent

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128, 72))
        self.rect = self.image.get_rect()
        self.y_speed = 2

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

        # Store the trail
        self.trail = []

        # Set the initial color
        self.color = self.random_color()
        self.image.fill(self.color)

    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        self.rect.y += self.y_speed

        # Prevent the player from going off the screen
        if self.rect.bottom > self.scene.bottom:
            self.rect.y = self.scene.top

        # Add the current position to the trail
        self.trail.append((self.rect.topleft, self.color))

        # Limit the trail length
        if len(self.trail) > 500:
            self.trail.pop(0)

    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1280, 720))

# Create players
players = pygame.sprite.Group(
    *[Player(i * 128, 100) for i in range(10)]
)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for player in players:
                    player.change_color()

    # Update players
    players.update()

    # Draw players and their trails
    screen.fill((255, 255, 255))  # Fill the screen with white
    for player in players:
        for pos, color in player.trail:
            pygame.draw.rect(screen, color, (pos, player.image.get_size()))
    players.draw(screen)

    # Flip the display
    pygame.display.flip()

pygame.quit()
