#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
vsl = violator_songs_list
summ = vsl[3][1] + vsl[5][1] + vsl[8][1]
summ_1 = toFixed(summ, 2)
print("Три песни звучат " + str(summ_1) + " минут")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
vsd = violator_songs_dict
# print(vsd['Sweetest Perfection'])
summ_2 = vsd['Sweetest Perfection'] + vsd['Policy of Truth'] + vsd['Blue Dress']
summ_3 = toFixed(summ_2, 2)
print("А другие три песни звучат " + str(summ_3) + " минут")