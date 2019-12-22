import simple_draw as sd


def tree(tree_x_cor, tree_y_cor, color, tree_angle, branch_angle, branch_length, trunk_length, branch_width):
    import random

    def draw_branches(start_point, angle, length):
        if length < 3:
            return
        angle_delta = branch_angle
        delta_minus = angle_delta - (0.4 * angle_delta)
        delta_plus = angle_delta + (0.4 * angle_delta)
        random_angle_change = sd.random_number(a=delta_minus, b=delta_plus)

        length_delta = .75
        length_minus = length_delta - (0.2 * length_delta)
        length_plus = length_delta + (0.2 * length_delta)
        random_length_change = random.random() * (length_minus - length_plus) + length_plus

        next_angle_right = angle - random_angle_change
        next_angle_left = angle + random_angle_change
        next_length = length * random_length_change

        branch_right = sd.get_vector(start_point=start_point, angle=next_angle_right, length=next_length, width=2)
        branch_right.draw(color=color)
        branch_left = sd.get_vector(start_point=start_point, angle=next_angle_left, length=next_length, width=2)
        branch_left.draw(color=color)

        next_point_right = branch_right.end_point
        next_point_left = branch_left.end_point
        draw_branches(start_point=next_point_right, angle=next_angle_right, length=next_length)
        draw_branches(start_point=next_point_left, angle=next_angle_left, length=next_length)

    sd.start_drawing()
    root_point = sd.get_point(x=tree_x_cor, y=tree_y_cor)
    trunk = sd.get_vector(start_point=root_point, angle=tree_angle, length=trunk_length, width=branch_width)
    trunk.draw(color=color)
    draw_branches(start_point=trunk.end_point, angle=tree_angle, length=branch_length)

    # рисуем яблоки на дереве


def apples(color):
    for x in range(850, 1250, 100):
        point = sd.get_point(x=x, y=350)
        sd.circle(center_position=point, radius=15, color=sd.COLOR_GREEN, width=0)
        sd.sleep(0.05)
        sd.circle(center_position=point, radius=15, color=color, width=0)

    sd.finish_drawing()
