import time
from settings import *
import pygame
from timer import Timer

class Floor:
    def __init__(self, num_of_floor) -> None:
        self.time_to_wait = None  # timer-object with the time nedded to wait
        self.num_of_floor = num_of_floor
        self.y_position = WINDOW_SIZE[1] - \
            (HEIGHT_FLOOR * (self.num_of_floor+1))
        self.button = None # a rect - object

    def color_button(self):
        # Determine the color of the floor button based on the timer status
        if not self.time_to_wait or not self.time_to_wait.time_left():# there no eevetor on the way
            return BUTTON_COLOR
        return GREEN

    def Prepare_for_arrival(self, time):
        # Update the self.timer to the "time to arrival"  - recived from the building when the floor request an elevator
        self.time_to_wait = Timer(time)
        
    def draw_line(self, window):
        # Draw a line between floors on the building window
        if self.y_position > 0: #all the floors exept the top floor
            pygame.draw.line(window, BLACK, (0, self.y_position+HEIGHT_BLACK_LINE / 2),
                            (BUILDING_WIDTH, self.y_position + HEIGHT_BLACK_LINE / 2), HEIGHT_BLACK_LINE)

    def draw_timer(self, window):
         # Draw the timer on the floor if it's instantiated and running
        if self.time_to_wait:  # the timer instantiate
            if self.time_to_wait.time_left():  # the clock is runing
                time_now = str(self.time_to_wait.time_left())
                # one digit after the point
                time_now = time_now[:time_now.find(".") + 2]
                font = pygame.font.SysFont("Arial", int(FONT_SIZE_TIMER))
                txt_surf = font.render(time_now, True, RED,GREEN)
                # draw in the left of the floor
                window.blit(txt_surf, (0, self.y_position+HEIGHT_BLACK_LINE))

    def __calculate_button_width(self):
         # Calculate the width of the floor button based on the font size and the largest floor-number 
        font = pygame.font.SysFont("Arial", FONT_SIZE_BUTTON)
        text_surface = font.render(str(NUM_OF_FLOORS), True, BLACK)
        text_surface_rect = text_surface.get_rect()
        button_width = text_surface_rect.width
        return button_width
            
    def draw_button(self,window):
        # Draw the floor button on the building window
        color_button = self.color_button()#detemine the color
        button_width = self.__calculate_button_width()
        rect_button = pygame.Rect((BUILDING_WIDTH / 2) - button_width / 2, self.y_position + (HEIGHT_FLOOR+HEIGHT_BLACK_LINE)/2 - button_width/2
                           ,button_width , button_width )
        font = pygame.font.SysFont("Arial", FONT_SIZE_BUTTON)
        # create txt_surf with the floor number in black color
        txt_surf = font.render(str(self.num_of_floor), True, BLACK)
        rect_font = txt_surf.get_rect()
        #place the rect-txt_surf in the button center 
        rect_font.center = rect_button.center
        #draw the button with the num_floor
        pygame.draw.rect(window, color_button, rect_button)
        window.blit(txt_surf, rect_font)
        #save the button-rect-object// for future click detection
        self.button = rect_button

    def draw_floor(self, window):
        # Draw the entire floor including timer, button, and line
        self.draw_timer(window)
        self.draw_button(window)
        self.draw_line(window)