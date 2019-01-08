# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

int_2 = 0
int_3 = 0
int_4 = 0
int_5 = 0
int_6 = 0
int_7 = 0
int_8 = 0
int_9 = 0
i = 0
for i in array:
    if i % 2 == 0:
        int_2 = int_2 + 1
    if i % 4 == 0:
        int_4 = int_4 + 1
    if i % 6 == 0:
        int_6 = int_6 + 1
    if i % 8 == 0:
        int_8 = int_8 + 1
    if i % 3 == 0:
        int_3 = int_3 + 1
    if i % 5 == 0:
        int_5 = int_5 + 1
    if i % 7 == 0:
        int_7 = int_7 + 1
    if i % 9 == 0:
        int_9 = int_9 + 1
    i += 1

print('Кратно 2 : ', int_2)
print('Кратно 3 : ', int_3)
print('Кратно 4 : ', int_4)
print('Кратно 5 : ', int_5)
print('Кратно 6 : ', int_6)
print('Кратно 7 : ', int_7)
print('Кратно 8 : ', int_8)
print('Кратно 9 : ', int_9)
