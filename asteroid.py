import pygame
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