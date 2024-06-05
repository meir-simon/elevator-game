import pygame
from settings import *
from building import building
pygame.init()
building1 = building()
window_size = (building_width+(num_of_elevators * elevator_width), num_of_floors*height_floor)
if window_size[0] < 1800 or window_size[1] < 1000: 
   window = pygame.display.set_mode(window_size)
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
else:
   print("to much floors/elevators to the screen, buy tv screen")   



        



               



        

            












        


# if move up > current position = dest - (timer.last stop)*2
#if move down > current position = dest + (timer.last stop)*2
     



