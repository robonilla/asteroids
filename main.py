# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player as ply

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    player = ply.Player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()

