"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
m = 2
n = 3
x = 1
i = 1
c = False
while i < n :
    if i * m != x:
        i +=1 
    else:
        c = True
        break
if c == False:
    while i < m :
        if i * n != x:
            i +=1 
        else:
            c = True
            break
if c == True:
    print('Yes')
else :
    print('No')