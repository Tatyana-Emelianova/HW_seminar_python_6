# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# def fract ():
#     my_list = list(map(float, input().split()))
#     fractions = []
#     for i in range(len(my_list)):
#         fractions.append(round(my_list[i]%1,3))
#     print(fractions)
#     print(max(fractions) - min(fractions))

# fract ()

def fract ():
    my_list = list(map(float, input().split()))
    fractions = list(map(lambda x: round(x%1,3), my_list ))
    print(max(fractions) - min(fractions))
fract ()
