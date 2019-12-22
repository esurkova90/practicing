wall_length = []


def wall(color, start_x, start_y, side_y_size, side_x_size, brick_x_size, brick_y_size, width):
    import simple_draw as sd
    row = 0
    for y in range(start_y, side_y_size, brick_y_size):
        row += 1
        for x in range(start_x, side_x_size, brick_x_size):
            point_a = sd.get_point(x=x, y=y)
            point_b = sd.get_point(x=x + brick_x_size, y=y + brick_y_size)
            if row % 2 == 0:
                point_a = sd.get_point(x=x + (brick_x_size * .5), y=y)
                point_b = sd.get_point(x=x + (brick_x_size * 1.5), y=y + brick_y_size)
            sd.rectangle(left_bottom=point_a, right_top=point_b, color=color, width=width)

    # рисуем форму
    point_x = sd.get_point(x=start_x, y=start_y)
    house_length = x + (brick_x_size * 1.5)
    point_y = sd.get_point(x=house_length, y=y + brick_y_size)
    sd.rectangle(left_bottom=point_x, right_top=point_y, color=color, width=width)

    wall_length.append(house_length)
    wall_length.append(y)
