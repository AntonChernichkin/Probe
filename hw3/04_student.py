# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
needed_money = 0
total_needed_money = 0
for i in range(4):
    if i == 1:
        print("Траты на обучение во " + str(i+1) + " год " + str(round(expenses, 2)) + " рублей")
    else:
        print("Траты на обучение в " + str(i+1) + " год " + str(round(expenses, 2)) + " рублей")
    needed_money = expenses - educational_grant
    total_needed_money += needed_money
    expenses = expenses * 1.03
    if i == 1:
        print("Студенту надо попросить во " + str(i + 1) + " год обучения " + str(round(needed_money, 2)) + " рублей")
    else:
        print("Студенту надо попросить в " + str(i+1) + " год обучения " + str(round(needed_money, 2)) + " рублей")

print("Суммарно студенту нужно попросить " + str(round(total_needed_money, 2)) + " рублей на 4 года обучения")