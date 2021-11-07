# -*- coding: utf-8 -*-
import random as random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_point = sd.get_point(100, 100)


# radius = 50
# for _ in range(3):
#     sd.circle(center_position=center_point, radius=radius)
#     radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
colors = [sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

def bubble(center_point_def, step, radius, color):
    for _ in range(3):
        sd.circle(center_position=center_point_def, radius=radius, color=color, width=0)
        radius -= step


#
# bubble(center_point_def=center_point, step=5, radius=90)

# Нарисовать 10 пузырьков в ряд

# x = 0
# for _ in range(10):
#     x += 100
#     center_point = sd.get_point(x, 100)
#     bubble(center_point_def=center_point, step=5, radius=50)

# Нарисовать три ряда по 10 пузырьков

# for _ in range(3):
#     y = 0
#     y += 100
#     x = 0
#     for i in range(10):
#         x += 100
#         center_point = sd.get_point(x, y)
#         bubble(center_point_def=center_point, step=5, radius=50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(1000):
    point_100 = sd.random_point()
    step_100 = random.randint(2, 8)
    radius_100 = random.randint(2, 50)
    _n = random.randint(0, 5)
    color = colors[_n]
    print(radius_100, step_100)
    bubble(center_point_def=point_100, step=step_100, radius=radius_100, color=color)

sd.pause()
