import pygame
from settings import *
from building import Building

pygame.init()
my_building = Building()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Elevators Game")
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            click_position = pygame.mouse.get_pos()
            my_building.identify_clicks(click_position)
    # Fill the window with white background
    window.fill((WHITE))
    # Draw and update all building elements
    my_building.draw_and_update_all(window)
    # Update the display
    pygame.display.update()
pygame.quit()