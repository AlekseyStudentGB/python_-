"""
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
my_list = input('введите трехзначное число')  
print(type(my_list))
print(int(my_list[0]) + int(my_list[1]) + int(my_list[2]))