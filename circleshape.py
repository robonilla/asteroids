import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self,circle_shape):
        distance_between = self.position.distance_to(circle_shape.position)
        max_distance = self.radius + circle_shape.radius
        return distance_between < max_distance
    
    def set_velocity(self, vel):
        self.velocity = vel