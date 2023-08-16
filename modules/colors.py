from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

color_sensor_floor_left = ColorSensor(Port.S1)
color_sensor_floor_right = ColorSensor(Port.S2)

cor_vista = "BRANCO"

def red_left():
    return color_sensor_floor_left.rgb()[0]

def green_left():
    return color_sensor_floor_left.rgb()[1]

def blue_left():
    return color_sensor_floor_left.rgb()[2]

def red_right():
    return color_sensor_floor_right.rgb()[0]

def green_right():
    return color_sensor_floor_right.rgb()[1]

def blue_right():
    return color_sensor_floor_right.rgb()[2]

# -------------------------------------------------------------

range_max_black_left = [26, 25, 20]
range_min_black_left = [0, 0, 0]

range_max_black_right = [27, 27, 32]
range_min_black_right = [0, 0, 2]

def is_black_left():
    return range_min_black_left[0] < red_left() < range_max_black_left[0] and range_min_black_left[1] < green_left() < range_max_black_left[1] and range_min_black_left[2] < blue_left() < range_max_black_left[2]

def is_black_right():
    return range_min_black_right[0] < red_right() < range_max_black_right[0] and range_min_black_right[1] < green_right() < range_max_black_right[1] and range_min_black_right[2] < blue_right() < range_max_black_right[2]

def is_black():
    return is_black_left() and is_black_right()

# -------------------------------------------------------------

range_max_yellow_left = [86, 85, 42]
range_min_yellow_left = [56, 55, 12]

range_max_yellow_right = [85, 85, 58]
range_min_yellow_right = [55, 55, 28]

def is_yellow_left():
    return range_min_yellow_left[0] < red_left() < range_max_yellow_left[0] and range_min_yellow_left[1] < green_left() < range_max_yellow_left[1] and range_min_yellow_left[2] < blue_left() < range_max_yellow_left[2]

def is_yellow_right():
    return range_min_yellow_right[0] < red_right() < range_max_yellow_right[0] and range_min_yellow_right[1] < green_right() < range_max_yellow_right[1] and range_min_yellow_right[2] < blue_right() < range_max_yellow_right[2]

def is_yellow():
    return is_yellow_left() and is_yellow_right()

# -------------------------------------------------------------

range_max_blue_left = [30, 41, 95]
range_min_blue_left = [0, 11, 65]

range_max_blue_right = [32, 45, 110]
range_min_blue_right = [2, 15, 80]

def is_blue_left():
    return range_min_blue_left[0] < red_left() < range_max_blue_left[0] and range_min_blue_left[1] < green_left() < range_max_blue_left[1] and range_min_blue_left[2] < blue_left() < range_max_blue_left[2]

def is_blue_right():
    return range_min_blue_right[0] < red_right() < range_max_blue_right[0] and range_min_blue_right[1] < green_right() < range_max_blue_right[1] and range_min_blue_right[2] < blue_right() < range_max_blue_right[2]

def is_blue():
    return is_blue_left() and is_blue_right()

# -------------------------------------------------------------

range_max_red_left = [77, 33, 26]
range_min_red_left = [47, 3, 0]

range_max_red_right = [90, 32, 33]
range_min_red_right = [60, 2, 3]

def is_red_left():
    return range_min_red_left[0] < red_left() < range_max_red_left[0] and range_min_red_left[1] < green_left() < range_max_red_left[1] and range_min_red_left[2] < blue_left() < range_max_red_left[2]

def is_red_right():
    return range_min_red_right[0] < red_right() < range_max_red_right[0] and range_min_red_right[1] < green_right() < range_max_red_right[1] and range_min_red_right[2] < blue_right() < range_max_red_right[2]

def is_red():
    return is_red_left() and is_red_right()

# -------------------------------------------------------------

def is_wall():
    return (is_black_left() and is_yellow_right()) or (is_yellow_left() and is_black_right())