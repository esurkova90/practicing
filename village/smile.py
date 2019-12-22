import simple_draw as sd

#
# colors = {
#     "white": sd.COLOR_WHITE,
#     "black": sd.COLOR_BLACK,
#     "red": sd.COLOR_RED,
#     "orange": sd.COLOR_ORANGE,
#     "yellow": sd.COLOR_YELLOW,
#     "green": sd.COLOR_GREEN,
#     "cyan": sd.COLOR_CYAN,
#     "blue": sd.COLOR_BLUE,
#     "purple": sd.COLOR_PURPLE,
#     "dark orange": sd.COLOR_DARK_ORANGE
# }

_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
           sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

blink_index = 0


def smile(center_point, color, width):
    # голова
    radius = 50
    sd.circle(center_position=center_point, radius=radius, color=color, width=width)

    # глаз левый
    point = sd.get_point(x=center_point.x - 20, y=center_point.y + 10)
    radius = 5
    sd.circle(center_position=point, radius=radius, color=color, width=width)

    # глаз правый
    point = sd.get_point(x=center_point.x + 20, y=center_point.y + 10)
    radius = 5
    sd.circle(center_position=point, radius=radius, color=color, width=width)

    # улыбка
    point_1 = sd.get_point(x=center_point.x - 25, y=center_point.y - 15)
    point_2 = sd.get_point(x=center_point.x - 15, y=center_point.y - 20)
    point_3 = sd.get_point(x=center_point.x + 15, y=center_point.y - 20)
    point_4 = sd.get_point(x=center_point.x + 30, y=center_point.y - 15)
    point_list = point_1, point_2, point_3, point_4
    sd.lines(point_list=point_list, color=color, closed=False, width=width)


def smile_blinks(center_point):
    global blink_index
    # smile(center_point=center_point, color=color, width=5)
    smile(center_point=center_point, color=_colors[blink_index], width=5)
    blink_index += 1
    if blink_index == len(_colors):
        blink_index = 0
