import pygame

from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
