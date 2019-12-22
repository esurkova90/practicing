# -*- coding: utf-8 -*-

# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
from village import house, snowflake, tree, rainbow, smile, sun

sd.resolution = 1400, 800
side_x_size = 600
side_y_size = 400
sd.start_drawing()

sun.sun()
rainbow.rainbow(rainbow_x=300, rainbow_y=-50, radius=1150, width=8)
tree.tree(tree_x_cor=1000, tree_y_cor=100, color=sd.COLOR_GREEN, tree_angle=90, branch_angle=30, branch_length=90,
          trunk_length=100, branch_width=2)
snowflake.snowflakes(snowflake_x_cor=100, snowflake_y_cor=130, length=15, snowflakes_count=15)
house.house(color=sd.COLOR_YELLOW, start_x=250, start_y=100, side_y_size=side_y_size, side_x_size=side_x_size,
            brick_x_size=80, brick_y_size=50, width=1)
center_point = sd.get_point(x=side_x_size / 1.5 + side_y_size / 6, y=side_y_size / 2 + side_y_size / 6)
smile.smile(center_point=center_point, color=sd.COLOR_PURPLE, width=5)
sd.finish_drawing()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
coordinates_snowflakes = []
while True:
    snowflake.snowfall(coordinates_snowflakes=coordinates_snowflakes)
    for coordinate_snowflake in coordinates_snowflakes:
        coordinate_snowflake["y"] -= 10
    rainbow.rainbow_blink(rainbow_x=300, rainbow_y=-50, radius=1150, width=8)
    smile.smile_blinks(center_point=center_point)
    sun.sun_blink(color=sd.COLOR_PURPLE)
    tree.apples(color=sd.COLOR_ORANGE)
    sd.sleep(0.01)
    if sd.user_want_exit():
        break

# зачёт!
