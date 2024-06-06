import time
import pygame
from settings import *
from timer import timer
from elevator import elevator
from floor import Floor


class Building:
    def __init__(self):
        # Insantiate floors and elevators
        self.floors = [Floor(x) for x in range(NUM_OF_FLOORS)]
        self.elevators = [elevator(x) for x in range(NUM_OF_ELEVATORS)]
        # send all elevators to the first floor
        for elev in self.elevators:
            elev.dest_floor = self.floors[0].y_position 


    def identify_clicks(self, click_position):
             # Check if a floor button is clicked
            for fl in self.floors:
                if fl.button.collidepoint(click_position):
                    self.call_elevator(fl)
                    return
        

    def call_elevator(self, floor):  # get an object floor
        # getting the coordinate of the requesting floor
        floor_y = floor.y_position
        flag = True
         # checks for a double call
        for i in [elev.current_calles for elev in self.elevators]: 
            if floor_y in i:
                flag = False
        # checks if there is elavator in the floor       
        for elevator in self.elevators:
            if elevator.dest_floor == floor_y:
                flag = False
                
        if flag:
            #find the index of the faster elevetor, and the time to arrival
            elevator_chosen, min_time = ind_min(
                [elevator.time_to_floor(floor_y) for elevator in self.elevators])
            #send to the elevator object a call to the y coordinate of the floor  
            elevator = self.elevators[elevator_chosen]
            elevator.get_call(floor_y)
             # instantiate timer with the time to arrival
            floor.update_time(min_time)
           

    def draw_and_update_all(self, window):
        # Draw the building background
        Building_img = pygame.image.load(IMG_BUILDING_PATH)
        Building_img = pygame.transform.scale(Building_img, (BUILDING_WIDTH, WINDOW_SIZE[1]))
        window.blit(Building_img, (0, 0))
         
        for element in self.floors:
            element.draw_floor(window)
        for element in self.elevators:
            element.update_position()
            element.draw_elevator(window)
