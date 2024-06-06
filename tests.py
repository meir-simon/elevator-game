# import pygame
from settings import *
# pygame.init()
# img_floor = pygame.image.load(r"building.jpg")
# img_elevator = pygame.image.load(r"elv.png")
# window_size = (building_width+(num_of_elevators * elevator_width), num_of_floors*(hight_floor))
# if window_size[0] < 1800 or window_size[1] < 1000:  
#    window = pygame.display.set_mode(window_size)
#    img_floor = pygame.transform.scale(img_floor,(building_width,window_size[1]))
#    img_elevator = pygame.transform.scale(img_elevator,(elevator_width,hight_floor))
   
   
  
#    pygame.display.set_caption("elevators game")

#    running = True
#    while running:
#       # Handle events
#       for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#             running = False
#       window.fill((255, 255, 255))
#       window.blit(img_floor,(0,0))
      
#       for x in range(num_of_floors):
#          rect = pygame.Rect((building_width/2)-20,(x*hight_floor)+hight_black_line ,building_width/3 ,hight_floor)
#          pygame.draw.line(window,(0,0,0),(0,x*(hight_floor)+(hight_black_line/2)),(building_width,x*(hight_floor)+(hight_black_line/2)),hight_black_line)
#          pygame.draw.rect(window,(0,255,0),rect)

#          font = pygame.font.SysFont("Arial", 10) 
#          txtsurf = font.render("08:53",True,(255,0,0),(0,255,0))
#          window.blit(txtsurf,(0,hight_floor*(x+0.5))) 

#       for x in range(num_of_elevators):
#          window.blit(img_elevator,(building_width+x*elevator_width,window_size[1]-hight_floor))



#       pygame.display.update()
#    pygame.quit()
# else:
#    print("to much floors/elevators to the screen")
a = 3.8
b=  a//2
print(type(b))