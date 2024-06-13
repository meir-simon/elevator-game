import time
from settings import *
import pygame
from timer import Timer

class Elevator:
    def __init__(self,num_of_elevator) -> None:
        self.num_of_elevator = num_of_elevator
        self.y_position = WINDOW_SIZE[1] - (HEIGHT_FLOOR) # top-left y_coordinate 
        self.x_position = BUILDING_WIDTH+self.num_of_elevator*ELEVATOR_WIDTH
        self.current_calles = [] # List of floors where elevator has been called
        self.time_to_available = Timer(0) # Timer for time until the elevator will be free to move
        self.moving = False
        self.time_to_stop_dealey = None # Timer for the delay before starting again  
        self.direction_of_motion = 0 # Direction of motion of the elevator //negative or positive number
        self.dest_floor =  None # y_coordinate of destination floor
        self.exit_time = 0 # Time when the elevator starts moving from the last floor 
        self.exit_floor = None #Last Floor from which the elevator starts moving

    def last_stop(self):
        # Return the last floor the elevator will stop at, or its current position if no calls
        if self.current_calles:
            return self.current_calles[-1]    
        return self.y_position
    
    def time_to_floor(self,floor):
        """  
    Calculate the time required for the elevator to reach a specified floor.

    Parameters:
    floor (int): The y-coordinate of the target floor.

    Returns:
    float: The total time required for the elevator to reach the specified floor, considering its "time to available" and the disttance from the last stop to the target floor
    """
        time_to_available = self.time_to_available.time_left()
        if not time_to_available: # If it zero or less
            time_to_available = 0
        return time_to_available + abs((self.last_stop() - floor)/SPEED)
    
    def get_call(self,floor):
        # Handle a call to a specific floor (y-coordinate)
        self.time_to_available = Timer(self.time_to_floor(floor) + DELEAY_TIME) 
        self.current_calles.append(floor)

    def make_noise(self):
        # Play a sound when the elevator reaches its destination
        sound = pygame.mixer.Sound(SOUND_PATH)   
        sound.play()
    
    def update_position(self):
        if not self.moving and self.current_calles: #the elevator has to to move
            if not self.time_to_stop_dealey or not self.time_to_stop_dealey.time_left() :#the elevator is free to move
                self.moving = True
                self.exit_time = time.time()
                self.exit_floor = self.y_position
                self.dest_floor = self.current_calles[0]
                #1 for movnent up, -1 for movment down
                self.direction_of_motion = abs(self.dest_floor - self.exit_floor)/(self.dest_floor - self.exit_floor)
        elif self.moving:
            time_now = time.time()
            d_time = time_now - self.exit_time
            self.y_position = self.exit_floor + (self.direction_of_motion) * SPEED * d_time
            # checks if the elevator reched its dest, based on the equation x(t) = x0+vt
            if d_time >= abs((self.dest_floor-self.exit_floor)/SPEED):
                #remove the dest floor from the list of calls 
                self.current_calles.pop(0)
                self.moving = False
                self.time_to_stop_dealey = Timer(DELEAY_TIME)
                self.make_noise()

    def draw_elevator(self,window):
         # Draw the elevator on the window
        pic = pygame.image.load(ELEVATOR_PIC)
        #Fits the elevator image
        pic = pygame.transform.scale(pic,(ELEVATOR_WIDTH,ELEVATOR_WIDTH)) 
        window.blit(pic,(self.x_position,round(self.y_position)))