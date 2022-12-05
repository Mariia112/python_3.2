#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример: - 45 -> 101101
#          - 3 -> 11
#          - 2 -> 10

num = int(input('Ввести число для преобразования: '))

def Convertation (binary_num):
    if int(binary_num) >= 2:
        return str(Convertation(int(binary_num/2))) + str(binary_num % 2)
    if int(binary_num) == 1:
        return '1'

print (Convertation(num))