import pygame
black = (0,0,0)

class Brick(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.color = color
    self.width = width
    self.height = height
    self.image = pygame.Surface([width, height])
    self.image.fill(black)
    self.image.set_colorkey(black)

    self.rect = self.image.get_rect()

  def draw(self):
      pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])  