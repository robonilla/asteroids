import pygame
import random
from circleshape import CircleShape
from constants import *

# Class for player
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position,self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        first_asteroid_vel = self.velocity.rotate(angle) * 1.2
        second_asteroid_vel = self.velocity.rotate(-angle) *1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        first_asteroid.velocity = first_asteroid_vel
        second_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        second_asteroid.velocity = second_asteroid_vel
        