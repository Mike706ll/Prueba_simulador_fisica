import sys
import pygame as pg
from radius_vector import Radius_vector
import settings as sts
from math import cos, sin
from math_functions import s_to_v

def update_resultant(vectors, res_vector):
    res_vector.end_x, res_vector. end_y = 0.0, 0.0
    for vector in vectors:
        res_vector.add(vector)

def check_events(sum_button, clear_button, vectors, res_vector):
    """
    Respond to keypresses and mouse events.
    """
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                check_mouse(mouse_x, mouse_y, sum_button, clear_button, vectors, res_vector)

def check_mouse(mouse_x, mouse_y, sum_button, clear_button, vectors, res_vector):
    """
    React to mouse press events.
    """
    button_clicked_sum = sum_button.rect.collidepoint(mouse_x, mouse_y)
    button_clicked_clear = clear_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked_sum:
        sts.res_state = True
    elif button_clicked_clear:
        clear_vectors(vectors, res_vector)
    else:
        vector = Radius_vector(s_to_v(mouse_x, mouse_y), 'normal')
        vectors.append(vector)
        update_resultant(vectors, res_vector)

def clear_vectors(vectors, res_vector):
    """
    Clear the screen of all vectors and sets relutant vector to zero and make it not visible.
    """
    sts.res_state = False
    res_vector.end_x, res_vector.end_y = 0, 0
    vectors.clear()

def update_screen(screen, sum_button, clear_button, vectors, res_vector):
    """
    Update images on the screen and flip to the new screen
    """
    screen.fill(sts.bg_color)
    draw_axes(screen)

    sum_button.draw_button()
    clear_button.draw_button()

    for vector in vectors:
        vector.draw_vector(screen)
    
    if sts.res_state:
        res_vector.draw_vector(screen)

    pg.display.flip()

def draw_axes(screen):
    """
    Draw the cartesian axes at the the center of the screen
    """
    px1 = (0, sts.screen_height/2)
    px2 = (sts.screen_width, sts.screen_height/2)
    py1 = (sts.screen_width/2, 0)
    py2 = (sts.screen_width/2, sts.screen_height)
    pg.draw.line(screen, sts.axes_color, px1, px2, sts.axes_width)
    pg.draw.line(screen, sts.axes_color, py1, py2, sts.axes_width)
