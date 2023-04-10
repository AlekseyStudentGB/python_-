"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""
bilet_num = input('Введите номер билета -> ')
# без цикла
# if int(bilet_num[0]) + int(bilet_num[1]) + int(bilet_num[2]) == int(bilet_num[3]) + int(bilet_num[4]) + int(bilet_num[5]):
#     print('Yes')
# else :
#     print('No')

# С циклом
bilet_len = len(bilet_num)

i = 0
right = 0
left = 0
while i < bilet_len :
    if bilet_len % 2 == 0:
        if i < bilet_len / 2 :
            right += int(bilet_num[i])
            i += 1
        else :
            left += int(bilet_num[i])
            i += 1
    else:
        if i < bilet_len // 2:
            right += int(bilet_num[i])
            i += 1
        elif i == bilet_len // 2:
            i += 1
        else: 
            left += int(bilet_num[i])
            i += 1
if right == left:
    print('yes')
else:
    print('no')
