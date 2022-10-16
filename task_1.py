#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#СТАРОЕ РЕШЕНИЕ

import math
from operator import index

spisok = [2,3,5,9,3]
sum_elem = 0
for i in range(len(spisok)):
    if i %2 != 0:
        sum_elem += spisok[i]
print(f"сумма элементов из списка {spisok} cтоящих на нечетной позиции = {sum_elem}")

#НОВОЕ РЕШЕНИЕ

lst = [1,2,3,4,5]

print(sum(list(filter(lambda i:lst.index(i) % 2 == 0,lst))))

