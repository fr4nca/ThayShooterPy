import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50
y = 50
width = 40
height = 60
vel = 5 

run = True
while(run):
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= vel
  if keys[pygame.K_RIGHT]:
    x += vel
  if keys[pygame.K_DOWN]:
    y += vel
  if keys[pygame.K_UP]:
    y -= vel

  window.fill((0))

  pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
  pygame.display.update()


pygame.quit()