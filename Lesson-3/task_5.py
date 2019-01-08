# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
item = 0
index = 0

for idx,i in enumerate(array):
    if i < item:
        item = i
        index = idx


print(f'Максимальный отрицательрный элемент: {item} его позиция {index}')
