#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
xy_moscow = sites['Moscow'] #координаты Москвы из объекта sites
xy_london = sites['London'] #координаты Лондона из объекта sites
xy_paris = sites['Paris'] #координаты Парижа из объекта sites

Moscow_London = ((xy_moscow[0] - xy_london[0]) ** 2 + (xy_moscow[1] - xy_london[1]) ** 2) ** .5 #расстояние от Москвы до Лондона
Moscow_Paris = ((xy_moscow[0] - xy_paris[0]) ** 2 + (xy_moscow[1] - xy_paris[1]) ** 2) ** .5 #расстояние от Москвы до Парижа
Paris_London = ((xy_paris[0] - xy_london[0]) ** 2 + (xy_paris[1] - xy_london[1]) ** 2) ** .5 #расстояние от Лондона до Парижа

distances['Moscow'] = {}  #создание пустого ключа-объекта Москва
distances['Moscow']['London'] = Moscow_London #создание в подъобъекте Москва ключа Лондон с расстоянием до него от москвы
distances['Moscow']['Paris'] = Moscow_Paris
distances['London'] = {}
distances['London']['Moscow'] = Moscow_London
distances['London']['Paris'] = Paris_London
distances['Paris'] = {}
distances['Paris']['Moscow'] = Moscow_Paris
distances['Paris']['London'] = Paris_London;

print(distances)

