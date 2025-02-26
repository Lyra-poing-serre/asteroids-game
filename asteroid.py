import pygame.draw
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def slip(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rng_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_angle = self.velocity.rotate(rng_angle)
        second_angle = self.velocity.rotate(-rng_angle)

        first_child = Asteroid(self.position.x, self.position.y, new_radius)
        first_child.velocity = first_angle * 1.2

        second_child = Asteroid(self.position.x, self.position.y, new_radius)
        second_child.velocity = second_angle * 1.2
