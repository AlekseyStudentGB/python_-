"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

sum = int(input('Введите сумму чисел -> '))
multiplication = int(input('Введите произведение чисел -> '))
"""
i = 1
while i < sum+1:
    if sum - i == multiplication / i:
        print(f"первое число = {i}, второе число = {sum - i}")
        break
    if i == 1000:
        print("НЕТ РЕШЕНИЯ")
    i +=1
"""

d = sum ** (2) - 4 * multiplication  
if d > 0:
    x = (sum - d ** (0.5)) / 2
    y = (sum + d ** (0.5)) / 2
    if x == int(x):
        print(f"первое число = {y}, второе число = {int(x)}")
    else:
        print("НЕТ РЕШЕНИЯ")
elif d == 0:
    x = y = sum / 2 
    print(f"первое число = {y}, второе число = {int(x)}")
else:
    
    print("НЕТ РЕШЕНИЯ")