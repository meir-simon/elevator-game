import time
import pygame
from settings import *
from timer import timer
from elevator import elevator
from floor import floor

class building:
    def __init__(self):
        self.floors = [floor(x) for x in range(num_of_floors)]
        #self.bottun_centers_positions = []
        self.elevators = [elevator(x) for x in range(num_of_elevators)] 
    def identifies_clicks(self,click):
        if click[0] < building_width:
            num_floor = num_of_floors - 1 - (click[1] // (hight_floor+hight_black_line))
            floor = self.floors[num_floor]# floor contain the floor as object
            self.call_elevator(floor)
    def call_elevator(self,floor):#get an object floor
        floor_y = floor.y_position
        min_time, elevator_chosen = ind_min([elevator.time_to_floor(floor_y) for elevator in self.elevators])
        if min_time > 0:  #no elevator available in this floor
            print("meir")


            current_time = time.time()
            self.elevators[elevator_chosen].get_call(floor_y)
            floor.time_to_wait = timer( min_time) # instantiate timer with the time of whaiting
    def draw_and_update_all(self,window):
        img = pygame.image.load(img_building_path)
        img = pygame.transform.scale(img,(building_width,window_size[1]))
        window.blit(img,(0,0))
        for element in self.floors:
            element.draw_floor(window)
        for element in self.elevators:
            element.updat_position()
            element.draw(window)
