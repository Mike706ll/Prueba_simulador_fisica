import sys
import pygame as pg
import program_functions as pf
from settings import Settings
from button import Button
from radius_vector import Radius_vector

def run_game():
    # import general settings
    sets = Settings()
    
    # initializes screen 
    pg.init()
    screen = pg.display.set_mode((sets.screen_width, sets.screen_height))
    pg.display.set_caption("Suma de vectores")

    # Creating principal buttons
    sum_button = Button(screen, '+', (30, sets.screen_height - 30))
    clear_button = Button(screen, 'cls', (90, sets.screen_height - 30))
    
    # initilizes vector to work
    res_vector = Radius_vector(sets.center, 'resultant')
    vectors = []
    
    while True:
        pf.check_events(sets, sum_button, clear_button, vectors, res_vector)
        pf.update_screen(sets, screen, sum_button, clear_button, vectors, res_vector)

if __name__ == '__main__':
    run_game()