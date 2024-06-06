import time
from settings import *
import pygame
from timer import timer


class floor:
    def __init__(self, num_of_floor) -> None:
        self.time_to_wait = None  # object of timer with the time nedded to wait
        self.num_of_floor = num_of_floor
        self.y_position = WINDOW_SIZE[1] - \
            (HEIGHT_FLOOR * (self.num_of_floor+1))
        self.bottun_width = None # update according to the size font and the number of flors
        self.bottun = None # an object type rect

    def color_bottun(self):
        if not self.time_to_wait or not self.time_to_wait.time_left():# there no eevetor on the way
            return (170, 170, 170)
        return (0, 255, 0)

    def update_time(self, time):
        self.time_to_wait = timer(time)

    def draw_line(self, window):
        if self.y_position > 0: #all the floors exept the top floor
            pygame.draw.line(window, (0, 0, 0), (0, self.y_position+HEIGHT_BLACK_LINE / 2),
                            (BUILDING_WIDTH, self.y_position + HEIGHT_BLACK_LINE / 2), HEIGHT_BLACK_LINE)

    def draw_timer(self, window):

        if self.time_to_wait:  # the timer instantiate
            if self.time_to_wait.time_left():  # the clock is runing
                time_now = str(self.time_to_wait.time_left())
                # one digit after the point
                time_now = time_now[:time_now.find(".") + 2]
                font = pygame.font.SysFont("Arial", 10)
                # the current time from the timer in red on green
                txtsurf = font.render(time_now, True, (255, 0, 0), (0, 255, 0))
                # draw in the left of the floor
                window.blit(txtsurf, (0, self.y_position+HEIGHT_BLACK_LINE))

    def draw_bottun(self,window):
        color_bottun = self.color_bottun()
        rect_bottun = pygame.Rect((BUILDING_WIDTH / 2) - self.bottun_width / 2, self.y_position + (HEIGHT_FLOOR+HEIGHT_BLACK_LINE)/2 - self.bottun_width/2
                           ,self.bottun_width , self.bottun_width )
        font = pygame.font.SysFont("Arial", FONT_SIZE)
        # the current time from the timer in red on green
        txtsurf = font.render(str(self.num_of_floor), True, (0, 0, 0))
        rect_font = txtsurf.get_rect()
        rect_font.center = rect_bottun.center
        # draw in the left of the floor
        pygame.draw.rect(window, color_bottun, rect_bottun)
        window.blit(txtsurf, rect_font)
        self.bottun = rect_bottun


    def __calculate_button_width(self):
        font = pygame.font.SysFont("Arial", FONT_SIZE)
        text_surface = font.render(str(NUM_OF_FLOORS), True, (0, 0, 0))
        text_surface_rect = text_surface.get_rect()
        self.bottun_width = text_surface_rect.width

    def draw_floor(self, window):
        self.__calculate_button_width()
        self.draw_timer(window)
        self.draw_bottun(window)
        self.draw_line(window)



 
