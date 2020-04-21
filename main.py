#https://www.youtube.com/watch?v=FfWpgLFMI7w
import sys
import pygame
import random
import math 
from pygame import mixer
import ship

# Initialize the pygame
pygame.init()

# Create the screen
#www.freepik.com
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')

# Background Sound

mixer.music.load('background.wav')
pygame.mixer.music.set_volume(0.05)
mixer.music.play(-1)

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
playerX_change = 0

#Enemy
num_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyImg = pygame.image.load('enemy.png')
for i in range(num_of_enemies):
  enemyX.append(random.randint(0,735))
  enemyY.append(random.randint(50,150))
  enemyX_change.append(4)
  enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0,800)
bulletY = playerY - 20
bulletX_change = 0
bulletY_change = 10
# Ready to fire
bullet_state = 'ready'

# Score
# dafont
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
testY = 10

# GameOver
overFont = pygame.font.Font('freesansbold.ttf',64)


def show_score(x, y):
  score = font.render("Score :" + str(score_value), True, (255,255,255))
  screen.blit(score, (x, y))



def game_over_text():
  overText = overFont.render("GAME OVER" + str(score_value), True, (255,255,255))
  screen.blit(overText, (200, 250))


def player(x, y):
  # To draw the player on the screen
  screen.blit(playerImg, (x, y))


def enemy( x , y ):
  # To draw the player on the screen
  screen.blit(enemyImg, (x, y))


def fire_bullet(x,y):
 # We use global keyword to read and write a global variable inside a function.
  global bullet_state
  bullet_state ='fire'
  screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
  if distance <27:
    return True
  else:
    return False


#Game Loop
running = True
#screen.blit(background,(0, 0))
# Define a clock to set limit the fps
clock = pygame.time.Clock()

enemy = ship.EnemyShip('enemy.png', 400,100,4,1,1)

while running:
  #screen.fill((150,170,190)) 
  screen.blit(background,(0, 0)) #Need fix to speed up
  for event in pygame.event.get():
    #If the pygame quit event is called the whilw loop breaks
    if event.type == pygame.QUIT:  
      running = False
      pygame.quit()
      sys.exit(0)
      
  # If keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
      #print("A key is pressed")
      if event.key == pygame.K_LEFT:
        #print("Left arrow is pressed")
        playerX_change = -5
      if event.key == pygame.K_RIGHT:
        #print("Right arrow is pressed")
        playerX_change = 5
      if event.key == pygame.K_SPACE and bullet_state == 'ready': 
        # Get ship current position
        bulletX = playerX
        fire_bullet(bulletX,bulletY)
        bullet_sound = mixer.Sound('laser.wav')
        bullet_sound.set_volume(0.05)
        bullet_sound.play()
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
       # print("Keystoke has been released")
        playerX_change = 0
 

  enemy.update(screen)

  # Checking boundaries of spaceship so it doesn't go out of bounds
  playerX += playerX_change
  if playerX <=0: playerX =0
  if playerX >=736: playerX =736
  
  
  

      
    
      
  #bullet movement
  if bulletY <=0:
    bulletY = playerY - 20
    bullet_state = 'ready'
  if bullet_state is 'fire':
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
  player(playerX, playerY)
  show_score(textX, testY)

  
  pygame.display.update() # Updates the display on the srcreen

  clock.tick(60)
  # print(clock.get_fps())
  # print()
  
  
  