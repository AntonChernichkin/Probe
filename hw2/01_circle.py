#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
Pi = 3.1415926
S = round(Pi * radius ** 2, 4)
print(S)

# Pi = 3.1415926
# S = Pi * radius ** 2
# S = toFixed(S, 4)
# print(S)

# Далее, пусть есть координаты точки
point = (23, 34)

# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
# Расстояние между точками. d =√((х₂ - х₁ )² + (у₂- у₁ )²+(z₂ - z₁)²
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код
d = round(((point[0]) ** 2 + (point[1]) ** 2) ** .5, 4)
print(d)
print(d < radius)
# d = ((point[0] - 0) ** 2 + (point[1] - 0) ** 2) ** 0.5
# print(d)
# print(d < radius)
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код
d = round(((point_2[0]) ** 2 + (point_2[1]) ** 2) ** .5, 4)
print(d)
print(d < radius)

# d = ((point_2[0] - 0) ** 2 + (point_2[1] - 0) ** 2) ** 0.5
# print(d)
# print(d < radius)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False

