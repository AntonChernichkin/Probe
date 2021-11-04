#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Антон", "Варя", "Леброн", "Элвуня"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
]

my_family_height.append(["Антон", 197])
my_family_height.append(["Варя", 163])
my_family_height.append(["Леброн", 70])
my_family_height.append(["Элвуня", 15])
# print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост котца - " + str(my_family_height[0][1]) + " см")
print("Рост котоматери - " + str(my_family_height[1][1]) + " см")
print("Рост котодетя - " + str(my_family_height[2][1]) + " см")
print("Рост пернадетя - " + str(my_family_height[3][1]) + " см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

family_height = 0
for i in range(4):
    family_height += my_family_height[i][1]

print("Общий рост моей семьи - " + str(family_height) + " см")


















# s = 0
# for i in range(3):
#     s += my_family_height[i][1]
# print("Общий рост моей семьи - " + str(s) + " см")
