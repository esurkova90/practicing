import simple_draw as sd


# coordinates_snowflakes = []

def snowflakes(snowflake_x_cor, snowflake_y_cor, length, snowflakes_count):
    coordinates_snowflakes = []
    for _ in range(snowflakes_count):
        coordinate_snowflake = {
            "x": sd.random_number(snowflake_x_cor - 70, snowflake_x_cor + 70),
            "y": sd.random_number(snowflake_y_cor - 20, snowflake_y_cor + 20),
            "length": length,
        }
        coordinates_snowflakes.append(coordinate_snowflake)

    for coordinate_snowflake in coordinates_snowflakes:
        sd.start_drawing()
        point = sd.get_point(x=coordinate_snowflake["x"], y=coordinate_snowflake["y"])
        sd.snowflake(center=point, length=coordinate_snowflake["length"])
        sd.finish_drawing()


def snowfall(coordinates_snowflakes):
    coordinate_snowflake = {
        "x": sd.random_number(30, 130),
        "y": sd.random_number(400, 500),
        "length": sd.random_number(10, 20),
    }
    coordinates_snowflakes.append(coordinate_snowflake)

    for coordinate_snowflake in coordinates_snowflakes:
        sd.start_drawing()
        random_change_x = sd.random_number(1, 2)
        if random_change_x == 1:
            coordinate_snowflake["x"] -= 2
            point_invisible = sd.get_point(x=coordinate_snowflake["x"] + 2, y=coordinate_snowflake["y"] + 10)
        else:
            coordinate_snowflake["x"] += 2
            point_invisible = sd.get_point(x=coordinate_snowflake["x"] - 2, y=coordinate_snowflake["y"] + 10)
        sd.snowflake(center=point_invisible, length=coordinate_snowflake["length"], color=sd.background_color)
        point = sd.get_point(x=coordinate_snowflake["x"], y=coordinate_snowflake["y"])
        if coordinate_snowflake["y"] <= 100:
            coordinate_snowflake["y"] += 400
        sd.snowflake(center=point, length=coordinate_snowflake["length"])
        sd.finish_drawing()
