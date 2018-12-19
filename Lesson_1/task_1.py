#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input("Введите трёхзначное целое число")
number_1 = int(number[0])
number_2 = int(number[1])
number_3 = int(number[2])
summa = number_1 + number_2 + number_3
proiz_nie = number_1 * number_2 * number_3
print(f'Сумма введённых целых чисел :  {summa}')
print(f'Произведение введённых чисел : {proiz_nie}')
