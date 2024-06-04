import time
from settings import *
import pygame
class floor:
    def __init__(self,num_of_floor) -> None:
        self.time_to_wait = None #object of timer with the time nedded to wait
        self.num_of_floor = num_of_floor
        self.y_position = window_size[1] - (hight_floor * self.num_of_floor+1) 
    def color_bottun(self):
        if self.time_to_wait:
            return (0,255,0)
        return(255,0,0)


    def draw_line(self,window):
         pygame.draw.line(window,(0,0,0),(0,self.num_of_floor*(hight_floor)+(hight_black_line/2)),(building_width,self.num_of_floor*(hight_floor)+(hight_black_line/2)),hight_black_line)    

    # def draw_timer(self,window):
    #     if self.time_to_wait: # the clock is runing
    #         font = pygame.font.SysFont("Arial", 10) 
    #         txtsurf = font.render(str(self.time_to_wait.time_left()),True,(255,0,0),(0,255,0))#the current time from the timer in red on green
    #         window.blit(txtsurf,(0,hight_floor*(self.num_of_floor + 0.5)))# draw in the left of the floor 

    def draw_bottun(self,window):
        color_bottun = self.color_bottun()
        rect = pygame.Rect((building_width/2)-20,(self.num_of_floor*hight_floor)+hight_black_line ,building_width/3 ,hight_floor)
        pygame.draw.rect(window,color_bottun,rect)

    def draw_floor(self,window):
        #self.draw_timer(window)
        self.draw_bottun(window)
        self.draw_line(window)    
