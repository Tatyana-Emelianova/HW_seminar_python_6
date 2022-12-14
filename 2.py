#     Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# старое решение выполнено так чтобы средний элемент нечетного ряда оставался без множителя

# def inhalf ():
#     my_list = list(map(int, input().split()))
#     x = []
#     i = 0
#     b = 1
#     if len(my_list)%2==0:
#         my_len = int(len(my_list)/2)
#         while i<my_len:
#             x.append(my_list[i]*my_list[len(my_list)-b])
#             i +=1
#             b +=1
#     else:
#         my_len = int(len(my_list)//2+1)
#         while i<(my_len-1):
#             x.append(my_list[i]*my_list[len(my_list)-b])
#             i +=1
#             b +=1
#         x.append(my_list[my_len-1])
#     print(x)
# inhalf ()


def inhalf ():
    my_list = list(map(int, input().split()))
    
    # x = list((my_list[i]*my_list[(i+1)*-1]) for i in range(int((len(my_list)//2))))
    # if len(my_list)%2!=0:
    #     x.append(my_list[int(len(my_list)//2)])
    # print(x) - это условие делает новое решение
    # совпадающим с неточным старым - для нечетного ряда пары для среднего элемента нет. По корректному
    # условию задачи средний элемент пара сам для себя, так код короче
    
    print(list((my_list[i]*my_list[(i+1)*-1]) for i in range(int((len(my_list)//2))+1)))
    
inhalf ()

