import asyncio
import pygame
from strip import Strip


FPS = 25
SCREEN_SIZE = (1280, 720)

# Game loop
# Initialize Pygame


async def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)

    # Create strips
    strips = pygame.sprite.Group(
        *[Strip(i * 128, 0) for i in range(10)]
    )
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    for strip in strips:
                        strip.change_color()

        # Update strips
        strips.update()

        for strip in strips:
            for pos, color in strip.trail:
                pygame.draw.rect(screen, color, (pos, strip.image.get_size()))
        strips.draw(screen)

        # Flip the display
        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())
