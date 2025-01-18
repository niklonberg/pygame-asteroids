import pygame
from constants import *

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

  while True:
    for event in pygame.event.get():
      # Handle window close button event
      if event.type == pygame.QUIT:
        return
    
    screen.fill("black")
    pygame.display.flip()
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()