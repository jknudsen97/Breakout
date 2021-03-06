import pygame
black = (0,0,0)

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(black)
    self.image.set_colorkey(black)
    
    self.rect = self.image.get_rect()

  def moveLeft(self, pixels):
    self.rect.x -= pixels
    if self.rect.x < 0:
      self.rect.x = 0

  def moveRight(self, pixels):
    self.rect.x += pixels
    if self.rect.x > 500:
      self.rect.x = 500

  def draw(self, color, width, height):
    pygame.draw.rect(self.image, color, [0, 0, width, height])