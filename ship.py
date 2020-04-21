import pygame
#
# player.move
# player.update
# player.bullet.move
# player.bullet.update

# enemy.move
# enemy.update

# Actions -> move shoot
##
class Ship(object):
  ""
  
  ""
  def __init__(self, imagePath, posx, posy, speed, health):
    self.image = pygame.image.load(imagePath)
    self.posx = posx
    self.posy = posy
    #self.bounds = self.image.get_size()
    self.speed = speed
    self.health = health
    #self.gunDamage = gunDamage
    #self.gunCadence = gunCadence  
    #self.beenShoot = False
    # self.gun = Gun()
    
    
  def update(self, screen):
    self.actions()
    #self.gun.update(screen)
    #self.explode()
    self.draw(screen) 
    
  def actions(self):
    pass
    
  def explode(self):
    pass
    
  def draw(self, screen):
    screen.blit(self.image,(self.posx, self.posy))
    #screen.blit(self.gun.image, (self.posx, self.posy))

class EnemyShip(Ship):
    
  def actions(self):
    self.move()
   
  def move(self):
    self.posx += self.speed
    if self.posx < 0:
      self.speed = -self.speed
      self.posx += self.speed
    if self.posx > 736:
      self.speed = -self.speed
      self.posx += self.speed
    print(self.posx)




class PlayerShip(Ship):
    
  #self.gun = Gun(iii)  

  def actions(self):
    self.move()
    self.shoot()
  
  def move(self):
    key = pygame.keys.get_pressed()
    if key[K_LEFT]:
      self.posx += self.speed
    elif key[K_RIGHT]:
      self.posx -= self.speed

  def shoot(self):
    self.gun.update(screen)

  def set_gun(self, gunCadence, gunDamage):
    pass
        
      
      
class Gun(object):
      
  def __init__(self, imagePath, gunCadence, gunDamage):
    self.image = pygame.image.load(imagePath)
    self.posx = posx
    self.posy = posy
    #self.bounds = self.image.get_size()
    # self.speed = speed
    # self.health = health
    self.bulletsShoots = 0
    self.bullet = []
    self.bullet.append(Bullet())
  
  def update(self, screen):
    self.shoot()
    self.move()
    self.draw(screen)
    
  def shoot(self):
    key = pygame.keys.get_pressed()
    if self.bullet[bulletsShoots].timer > self.gunCadence and key[K_SPACE]:
      bullet[bulletsShoots] = Bullet()
      bullet[bulletsShoots].timer = 0
      self.bulletsShoots += 1
  
  
  def move(self):
    for i in range(bulletsShoots):
      self.bullet[i].posy -= self.speed
      if self.bullet[i].posy < 0:
        self.bullet.pop()
        self.bulletsShoots -= 1
  
  def draw(self, screen):
    screen.blit(self.image,(self.posx, self.posy))
 
  # def shoot(self):
    # if timer > self.gunCadence
      # key = pygame.keys.get_pressed()
      # if key[K_SPACE] or bulletTravelling:
        # self.posy += self.speed
        # timer = 0

class Bullet(object):
  pass