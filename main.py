import sys
import pygame as pg
import program_functions as pf
import settings as sts
from button import Button
from radius_vector import Radius_vector


def run_game():
    # initializes screen 
    pg.init()
    screen = pg.display.set_mode((sts.screen_width, sts.screen_height))
    pg.display.set_caption("Suma de vectores")

    # Creating principal buttons
    sum_button = Button(screen, '+', (30, sts.screen_height - 30))
    clear_button = Button(screen, 'cls', (90, sts.screen_height - 30))
    
    # initilizes vector to work
    res_vector = Radius_vector((0, 0), 'resultant')
    vectors = []
    
    while True:
        pf.check_events(sum_button, clear_button, vectors, res_vector)
        pf.update_screen(screen, sum_button, clear_button, vectors, res_vector)

if __name__ == '__main__':
    run_game()