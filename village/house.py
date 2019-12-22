def house(color, start_x, start_y, side_y_size, side_x_size, brick_x_size, brick_y_size, width):
    import simple_draw as sd
    from village import wall

    # вызываем стену

    wall.wall(color=color, start_x=start_x, start_y=start_y, side_y_size=side_y_size, side_x_size=side_x_size,
              brick_x_size=brick_x_size, brick_y_size=brick_y_size, width=width)

    house_length = wall.wall_length[0]
    end_y_wall = wall.wall_length[1]

    # рисуем крышу
    point_1 = sd.get_point(x=start_x, y=end_y_wall + brick_y_size)
    point_2 = sd.get_point(x=start_x + house_length * .3, y=side_y_size + + brick_y_size * 3)
    point_3 = sd.get_point(x=house_length, y=end_y_wall + brick_y_size)
    point_list = [point_1, point_2, point_3]
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_RED, width=0)

    # рисуем окно
    window_point = sd.get_point(x=side_x_size / 1.5, y=side_y_size / 2)
    sd.square(left_bottom=window_point, side=side_y_size / 3, color=sd.COLOR_WHITE, width=0)

    # рисуем землю
    point_1 = sd.get_point(x=0, y=0)
    point_2 = sd.get_point(x=0, y=100)
    point_3 = sd.get_point(x=sd.resolution[0], y=100)
    point_4 = sd.get_point(x=sd.resolution[0], y=0)
    point_list = [point_1, point_2, point_3, point_4]
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_ORANGE, width=0)
