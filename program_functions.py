import sys
import pygame as pg
from radius_vector import Radius_vector
import settings as sts
from math import cos, sin

# def t_coord(coord_x, coord_y):
#     new_x = coord_x + sts.screen_width/2
#     new_y = sts.screen_height/2 - coord_y
#     return new_x, new_y

# def s_coord(coord_x, coord_y):
#     new_x = coord_x - sts.screen_width/2
#     new_y = sts.screen_height/2 - coord_y
#     return new_x, new_y

def check_events(sets, sum_button, clear_button, vectors, res_vector):
    """
    Respond to keypresses and mouse events.
    """
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                button_clicked_sum = sum_button.rect.collidepoint(mouse_x, mouse_y)
                button_clicked_clear = clear_button.rect.collidepoint(mouse_x, mouse_y)
                if button_clicked_sum:
                    sets.res_state = True
                    sum_x, sum_y = 0, 0
                    for vector in vectors:
                        sum_x += vector.x - sets.center_x
                        sum_y += vector.y - sets.center_y
                    res_vector.x, res_vector.y = sets.center_x + sum_x, sets.center_y + sum_y
                elif button_clicked_clear:
                    clear_vectors(sets, vectors, res_vector)
                else:
                    vector = Radius_vector((mouse_x, mouse_y), 'normal')
                    vectors.append(vector)

def clear_vectors(sets, vectors, res_vector):
    sets.res_state = False
    res_vector.x, res_vector.y = sets.center
    vectors.clear()

def update_screen(sets, screen, sum_button, clear_button, vectors, res_vector):
    """
    Update images on the screen and flip to the new screen
    """
    screen.fill(sets.bg_color)
    draw_axes(sets, screen)

    sum_button.draw_button()
    clear_button.draw_button()

    for vector in vectors:
        vector.draw_vector(sets, screen)
    
    if sets.res_state:
        res_vector.draw_vector(sets, screen)

    pg.display.flip()


def draw_axes(sets, screen):
    """
    Draw the cartesian axes at the the center of the screen
    """
    px1 = (0, sets.screen_height/2)
    px2 = (sets.screen_width, sets.screen_height/2)
    py1 = (sets.screen_width/2, 0)
    py2 = (sets.screen_width/2, sets.screen_height)
    pg.draw.line(screen, sets.axes_color, px1, px2, sets.axes_width)
    pg.draw.line(screen, sets.axes_color, py1, py2, sets.axes_width)