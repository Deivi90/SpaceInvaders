#https://www.youtube.com/watch?v=FfWpgLFMI7w
import pygame

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))

#Tittle and Icon
#https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
#https://www.flaticon.com/
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480


def player():
  # To draw the player on the screen
  screen.blit(playerImg, (playerX, playerY))


#Game Loop
running = True
while running:
  for event in pygame.event.get():
    #If the pygame quit event is called the whilw loop breaks
    if event.type == pygame.QUIT:  
      running = False
      
  # RGB Values of the screen background  
  screen.fill((150,170,190))  
  player()
  pygame.display.update() # Updates the display on the srcreen
  
  
  
  
  
  