import pygame
from constants import *
from player import Player

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Initialize pygame engine/library
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0

  # Create game window with specified dimensions
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setups screen

  # Groups
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updateable, drawable)

  # Create player
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      # Handle window close button event
      if event.type == pygame.QUIT:
        return
    
    for obj in updateable:
      obj.update(dt)

    screen.fill("black")

    for obj in drawable:
      obj.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()