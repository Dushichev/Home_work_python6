#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


lst = list(map(int, input("Введите числа через пробел:\n").split(" ")))
exclusive_numbers = []

for i in lst:
    if i not in exclusive_numbers:                              # старое решение
        exclusive_numbers.append(i) 
print(f"Исходный список список: {lst}")
print(f"Список из неповторяющихся элементов: {exclusive_numbers}")


new_list =[el for el in lst if lst.count(el) == 1]              # Новое решение
print(new_list)



