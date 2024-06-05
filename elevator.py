import time
from settings import *
import pygame
from timer import timer
class elevator:
    def __init__(self,num_of_elevator) -> None:
        self.num_of_elevator = num_of_elevator
        self.y_position = window_size[1] - (height_floor)
        self.x_position = building_width+self.num_of_elevator*elevator_width
        self.current_calles = [] 
        self.time_until_rest = None
        self.moving = False
        self.time_to_stop_dealey = None
        self.dealey = False  
        self.direction_of_motion = 0
        self.dest_floor =  None
        self.exit_time = 0
        self.exit_floor = None

    def last_stop(self):
        if self.current_calles:
            return self.current_calles[-1]    
        return self.y_position
    
    def time_to_floor(self,floor):#get y coordinate of the floor
        time_until_rest = self.time_until_rest
        if not time_until_rest: # is none
            time_until_rest = 0
        else:
            time_until_rest = time_until_rest.time_left() 
            if not time_until_rest:
                time_until_rest = 0
        return time_until_rest + abs((self.last_stop() - floor)/speed)
    
    def get_call(self,floor): #get y coordinate of the top of the floor
        self.time_until_rest = timer(self.time_to_floor(floor) + deleay_time) 
        self.current_calles.append(floor)

    def make_noise(self):
        sound = pygame.mixer.Sound(sound_path)   
        sound.play()
    
    def updat_position(self):
        if not self.moving and self.current_calles: #need to move
            if not self.time_to_stop_dealey or not self.time_to_stop_dealey.time_left() :#the elevator is free
                self.dealey = False
                self.moving = True
                self.exit_time = time.time()
                self.dest_floor = self.current_calles[0]
                self.exit_floor = self.y_position
                self.direction_of_motion = self.dest_floor - self.exit_floor

                

        elif self.moving:
            time_now = time.time()
            self.y_position = self.exit_floor + (abs(self.direction_of_motion)/self.direction_of_motion) * speed * (time_now - self.exit_time)
            if (time_now - self.exit_time) >= abs((self.dest_floor-self.exit_floor)/speed)  :#the elevator reched the floor
                self.current_calles.pop(0)
                self.moving = False
                self.dealey = True
                self.time_to_stop_dealey = timer(deleay_time)
                self.make_noise()




    def draw_elevator(self,window):
        pic = pygame.image.load(elevator_pic)
        pic = pygame.transform.scale(pic,(elevator_width,height_floor)) 
        window.blit(pic,(self.x_position,round(self.y_position)))#need to make it int


