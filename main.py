import pygame
from settings import *
from building import building
pygame.init()
building1 = building()


window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("elevators game")

running = True
while running:
   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.MOUSEBUTTONUP:
         click = pygame.mouse.get_pos()
         building1.identifies_clicks(click)
   window.fill((255, 255, 255))
   building1.draw_and_update_all(window)
   pygame.display.update()
pygame.quit()



      



               



        

            












        


# if move up > current position = dest - (timer.last stop)*2
#if move down > current position = dest + (timer.last stop)*2
     



