import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()

white = (255,255,255)
red = (255,0,0)
orange = (255,100,0)
green = (52,255,51)
pink = (255,51,254)
blue = (58,51,255)
grey = (113,113,113)

score = 0
lives = 3
#Render the screen
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

all_sprites_list = pygame.sprite.Group()
#Render the paddle
paddle = Paddle(white, 100, 10)
paddle.rect.x = 300
paddle.rect.y = 380
#Render the ball
ball = Ball(pink, 10, 10)
ball.rect.x = 250
ball.rect.y = 360

#Create the brick wall
all_bricks = pygame.sprite.Group()
for i in range(5):
  brick1 = Brick(blue, 80, 30)
  brick2 = Brick(orange, 80, 30)
  brick3 = Brick(green, 80, 30)
  brick1.rect.x = 60 + i * 100
  brick2.rect.x = 60 + i * 100
  brick3.rect.x = 60 + i * 100
  brick1.rect.y = 60
  brick2.rect.y = 100
  brick3.rect.y = 140
  all_sprites_list.add(brick1)
  all_sprites_list.add(brick2)
  all_sprites_list.add(brick3)
  all_bricks.add(brick1)
  all_bricks.add(brick2)
  all_bricks.add(brick3)
  

all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_sprites_list.add(all_bricks)

loop = True

clock = pygame.time.Clock()
#Speed that the paddle moves
pygame.key.set_repeat(20)
while loop:
#Event loop
  for event in pygame.event.get(): 
    if event.type == pygame.quit:
      loop = False
    elif event.type==pygame.KEYDOWN:
      if event.key==pygame.K_q:
        loop = False

#Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
      paddle.moveRight(5)

    #Logic
    all_sprites_list.update()
    #If the ball hits a boundary
    if ball.rect.x>=590:
      ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=10:
      ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>390:
      ball.velocity[1] = -ball.velocity[1]
      lives -= 1
      if lives == 0:
        #Game Over Message
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, red)
        screen.blit(text, (100, 200))
        pygame.display.flip()
        pygame.time.wait(3000)
        #End the game
        loop = False

    if ball.rect.y<40:
      ball.velocity[1] = - ball.velocity[1]
      
    #Check if the ball hits the paddle
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    #Check if the ball hits a brick
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
        #You win message
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WIN!", 1, green)
        screen.blit(text, (100, 200))
        pygame.display.flip()
        pygame.time.wait(3000)
        loop = False
    #Draw
    screen.fill(grey)
    paddle.draw(white, 100, 10)
    ball.draw(pink, 10, 10)
    """brick1.draw()
    brick2.draw()
    brick3.draw()"""
    for entity in all_bricks:
      entity.draw()
    
    #Draw the score and lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (480,10))

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()