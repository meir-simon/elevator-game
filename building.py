import time
import pygame
from settings import *
from timer import timer
from elevator import elevator
from floor import floor


class building:
    def __init__(self):
        self.floors = [floor(x) for x in range(num_of_floors)]
        self.elevators = [elevator(x) for x in range(num_of_elevators)]
        for elev in self.elevators:# send all elevators to the first floor
            elev.dest_floor = self.floors[0].y_position 


    def identifies_clicks(self, click):
            for fl in self.floors:
                if fl.bottun.collidepoint(click):
                    self.call_elevator(fl)
                    return
        

    def call_elevator(self, floor):  # get an object floor
        floor_y = floor.y_position
        sign = True
        for i in [elev.current_calles for elev in self.elevators]:  # checks for a double call
            if floor_y in i:
                sign = False
               
        for elevator in self.elevators:  # checks if there is elavator in the floor
            if elevator.dest_floor == floor_y:
                sign = False
                
        if sign:
            elevator_chosen, min_time = ind_min(
                [elevator.time_to_floor(floor_y) for elevator in self.elevators])
            elevator = self.elevators[elevator_chosen]
            elevator.get_call(floor_y)
            # instantiate timer with the time of whaiting
            floor.update_time(min_time)

    def draw_and_update_all(self, window):
        img = pygame.image.load(img_building_path)
        img = pygame.transform.scale(img, (building_width, window_size[1]))
        window.blit(img, (0, 0))
        for element in self.floors:
            element.draw_floor(window)
        for element in self.elevators:
            element.updat_position()
            element.draw_elevator(window)
