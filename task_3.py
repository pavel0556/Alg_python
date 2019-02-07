import random
import task_2


def mediana(array):
    i = 0
    a = 0
    b = 0
    if len(array) % 2 != 0:
        return (array[len(array) // 2])
    else:
        a = len(array) // 2 - 1
        b = len(array) // 2
        i = (array[a] + data[b]) / 2
        return i

m=(int(input ("Введиет натуральное число :")))

if m<1:
        print("Введено не корректное значение")
else:
    array=[random.randint(1,m*3)for _ in range(2*m+1)]
    print(zadacha_2.mergeSort(array))
    print(mediana(array))
