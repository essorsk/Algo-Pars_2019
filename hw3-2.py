#2.	Во втором массиве сохранить индексы четных элементов первого массива.
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация начинается с нуля),
#т.к. именно в этих позициях первого массива стоят четные числа.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)
evens = []
i = 0
for el in array:
    if el % 2 == 0:
        evens.append(i)
    i += 1
        #evens.append(array.index(el)) - при повторении элементов в массиве индексы "слетают"
print(f'Индексы четных чисел массива: {evens}')
