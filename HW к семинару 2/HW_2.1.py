"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
""" 

import random

n = int(input('Укажите какое количество монет будем бросать -> '))
side_a, side_b = 0, 0
count = 0

while count < n :
    res_throw = random.randint(0,1)
    print(f"{count + 1}. {res_throw}")
    if res_throw == 0:
        side_a += 1
        count += 1
    else:
        side_b += 1
        count +=1 

if side_a > side_b:
    print(f'''чтобы все монетки были повернуты вверх одной и той же сторонойминимальное минимальное 
колличество монет, которые нужно перевернуть равно {side_b}''')
else:
    print(f'''чтобы все монетки были повернуты вверх одной и той же сторонойминимальное минимальное 
колличество монет, которые нужно перевернуть равно {side_a}''')