import settings as sts

def v_to_s(vec_x, vec_y):
    coord_x = sts.screen_width/2 + vec_x
    coord_y = sts.screen_height/2 - vec_y

    return coord_x, coord_y

def s_to_v(coord_x, coord_y):
    vec_x = coord_x - sts.screen_width/2
    vec_y = sts.screen_height/2 - coord_y

    return vec_x, vec_y