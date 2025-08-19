import pygame
from circleshape import CircleShape
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)
    pygame.display.set_caption("Asteroids")
    asteroid_field = AsteroidField()
    running = True
    clock = pygame.time.Clock()
    dt = 0
    x =  SCREEN_WIDTH/ 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background,(0,0))
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        asteroids:Asteroid
        for asteroid in asteroids:
            if asteroid.has_collided_with(player):
                print("Game Over!")
                return
        shot: Shot
        for shot in shots:
            for asteroid in asteroids:
             if asteroid.has_collided_with(shot):
                shot.kill()
                asteroid.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
