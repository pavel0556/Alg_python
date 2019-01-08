# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
pos_min_item = i
min_item = array[pos_min_item]
pos_max_item = i
max_item = array[pos_max_item]
while (i < len(array)):
    if (array[i] < min_item):
        pos_min_item = i
        min_item = array[pos_min_item]
    if (array[i] > max_item):
        pos_max_item = i
        max_item = array[pos_max_item]
    i += 1
array[pos_min_item] = max_item
array[pos_max_item] = min_item

print(f'Максимальное значение массива {max_item} его позиция {pos_max_item}')
print(f'Минимальное значение массива {min_item} его позиция  {pos_min_item}')

print(f'Массив после замены местами максимального и минимального значения \n{array}')
