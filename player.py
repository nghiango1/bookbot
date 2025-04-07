import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


# Class for game player objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, width=2)

    def update(self, dt):
        # sub-classes must override
        pass

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
