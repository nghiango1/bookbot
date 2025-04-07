# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroids.constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from asteroids.player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable_group, drawable_group)
    player = Player(x, y)

    while True:
        miliseconds_pass = clock.tick(60)
        seconds_pass = miliseconds_pass / 1000
        dt = seconds_pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable_group.update(dt)
        for thing in drawable_group:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
