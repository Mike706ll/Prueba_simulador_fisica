class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.center = (self.screen_width/2, self.screen_height/2)
        self.center_x = self.center[0]
        self.center_y = self.center[1]
        
        self.res_state = False

        self.bg_color = (255, 255, 255)
        self.res_color = (0, 0, 255)
        self.normal_color = (255, 0, 0)
        self.res_width = 3
        self.normal_width = 1

        self.axes_color = (0, 0, 0)
        self. axes_width = 3

        self.alpha = 0.0
screen_width = 1000
screen_height = 600