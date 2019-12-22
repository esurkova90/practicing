import simple_draw as sd

_is_invert_color = False
point = sd.get_point(x=200, y=650)


def sun():
    sd.circle(center_position=point, radius=50, color=sd.COLOR_YELLOW, width=0)

    for angle in range(60, 700, 40):
        ray = sd.get_vector(start_point=point, angle=angle, length=100, width=4)
        ray.draw()


def sun_blink(color):
    global _is_invert_color
    _color = color if _is_invert_color else sd.COLOR_YELLOW
    sd.circle(center_position=point, radius=50, color=_color, width=0)
    for angle in range(60, 700, 40):
        ray = sd.get_vector(start_point=point, angle=angle, length=100, width=4)
        ray.draw(color=_color)

    _is_invert_color = not _is_invert_color
