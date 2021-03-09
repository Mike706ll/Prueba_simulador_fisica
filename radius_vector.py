import pygame as pg
import math as mt
import sys

class Radius_vector:
    
    def __init__(self, end_point, type):
        self.x, self.y = end_point
        self.type = type

    def draw_vector(self, sets, screen):
        if self.type == "resultant":
            width = sets.res_width
            color = sets.res_color
        else:
            width = sets.normal_width
            color = sets.normal_color
        
        pg.draw.line(screen, color, (sets.screen_width/2, sets.screen_height/2),
                                     (self.x, self.y), width)
        
        a = -mt.cos(mt.pi/12)
        b = mt.sin(mt.pi/12)
        c = a
        d = -b
        alpha = mt.atan2(-self.y + sets.center_y, self.x - sets.center_x)
        # if alpha < 0:
        #     alpha = 2*mt.pi - alpha
   
        a1, b1 = a*mt.cos(alpha) - b*mt.sin(alpha), a*mt.sin(alpha) + b*mt.cos(alpha)
        c1, d1 = c*mt.cos(alpha) - d*mt.sin(alpha), c*mt.sin(alpha) + d*mt.cos(alpha)
        
        a1 *= 10
        b1 *= 10
        c1 *= 10
        d1 *= 10
        pg.draw.line(screen, color, (self.x + a1, self.y - b1),
                                     (self.x, self.y), width)
        pg.draw.line(screen, color, (self.x + c1, self.y - d1),
                                     (self.x, self.y), width)                         
        # m1 = (self.y - sets.center_y)/(self.x - sets.center_x)
        # m2 = (m1 + 0.26795)(1 - m1*0.26795)
        # O = 
        # pg.draw.line(screen, color, (sel.x, self.y), (), width)
