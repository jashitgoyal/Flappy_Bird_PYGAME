import pygame
pygame.init()

screen_width = 864;
screen_height = 936; 

clock = pygame.time.Clock()
fps = 60

screen  =  pygame.display.set_mode((screen_width,screen_height));
pygame.display.set_caption("FLAPPY BIRD");
# load images
bg = pygame.image.load('img/bg.png')
ground  = pygame.image.load("img/ground.png")
# game variables
run = True;
game_over = False;

ground_scroll = 0;
scroll_speed = 3
# game loop
while  run:
  clock.tick(fps)
  screen.blit(bg,(0,0))
  screen.blit(ground,(ground_scroll,768))
  ground_scroll=ground_scroll-scroll_speed;

  if abs(ground_scroll)>35:
    ground_scroll =0;

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

  pygame.display.update();

pygame.quit();
quit();

