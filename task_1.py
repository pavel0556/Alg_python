import random

array=[random.randint(-100,100) for _ in range(10)]
print(array)

def bubble (array):
    n=1
    while n < len(array):
        for i in range(len(array)-1):
            if array[i]> array [i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        n+=1
    return array

print(bubble(array))
