import pygame as pg
import math as mt
import settings as sts
from generic_vector import Generic_Vector
import sys

class Radius_vector(Generic_Vector):
    
    def __init__(self, end_point, type = 'normal'):
        super().__init__((0, 0), end_point)
        self.type = type
        if self.type == "resultant":
            self.width = sts.res_width
            self.color = sts.res_color

    def add(self, r_vector):
        self.end_x += r_vector.end_x
        self.end_y += r_vector.end_y

