#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример: - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

def minmax(list):
    max_min = []
    for i in range(len(list)):
        if list[i] % 1 != 0:
            max_min.append(list[i] % 1)
    return max(max_min) - min(max_min)


new_list = [1.10, 1.20, 3.10, 5, 10.01]
print(new_list)
result = minmax(new_list)
print(f'Ответ = {result:.2f}')