# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов массива: '))
list_1 = []

for i in range(n):
    list_1.append(i + 1)
print(list_1)

x = int(input('Введите искомое число: '))

count = 0
for i in range(n):
    if list_1[i] == x:
        count += 1
        
if count == 0:
    print('Такого числа нет в массиве.')
else: print(count)