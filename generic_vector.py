import pygame as pg
import settings as sts
import math as mt
from math_functions import v_to_s

class Generic_Vector:

    def __init__(self, initial_point, end_point):
        self.ini_x, self.ini_y = initial_point
        self.end_x, self.end_y = end_point
        self.color = sts.normal_color
        self.width = sts.normal_width

    def draw_vector(self, screen):
        c_ini_x, c_ini_y = v_to_s(self.ini_x, self.ini_y)
        c_end_x, c_end_y = v_to_s(self.end_x, self.end_y)
       
        pg.draw.line(screen, self.color, (c_ini_x, c_ini_y),
                     (c_end_x, c_end_y), self.width)
        self.draw_arrow(screen,  c_ini_x, c_ini_y, c_end_x, c_end_y)

    def draw_arrow(self, screen, c_ini_x, c_ini_y, c_end_x, c_end_y):
        a, b = -mt.cos(mt.pi/12), mt.sin(mt.pi/12)
        c, d = a, -b

        alpha = mt.atan2(-c_end_y + c_ini_y, c_end_x - c_ini_x)
        a1, b1 = 10*(a*mt.cos(alpha) - b*mt.sin(alpha)), 10*(a*mt.sin(alpha) + b*mt.cos(alpha))
        c1, d1 = 10*(c*mt.cos(alpha) - d*mt.sin(alpha)), 10*(c*mt.sin(alpha) + d*mt.cos(alpha))
        
        pg.draw.line(screen, self.color, (c_end_x + a1, c_end_y - b1),
                                     (c_end_x, c_end_y), self.width)
        pg.draw.line(screen, self.color, (c_end_x + c1, c_end_y - d1),
                                     (c_end_x, c_end_y), self.width)
                                     
