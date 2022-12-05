#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pari(list):
    new_list = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        new_list.append(list[i]*list[count])
        count -= 1
        i += 1
    return new_list

#list = [2, 3, 4, 5, 6]
# #или
list = [2, 3, 5, 6]
new_list = pari(list)
print(list)
print(new_list)
