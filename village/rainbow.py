import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
rainbow_colors_1 = rainbow_colors[::-1]


def rainbow(rainbow_x, rainbow_y, radius, width):
    point = sd.get_point(x=rainbow_x, y=rainbow_y)
    radius = radius
    for color in rainbow_colors_1:
        radius += 8
        sd.circle(center_position=point, radius=radius, color=color, width=width)


def rainbow_blink(rainbow_x, rainbow_y, radius, width):
    point = sd.get_point(x=rainbow_x, y=rainbow_y)
    radius = radius
    for color in rainbow_colors_1:
        radius += 8
        sd.circle(center_position=point, radius=radius, color=(color[0]*0.7, color[1]*0.7, color[2]*0.7), width=width)
        sd.sleep(0.05)
        sd.circle(center_position=point, radius=radius, color=color, width=width)
