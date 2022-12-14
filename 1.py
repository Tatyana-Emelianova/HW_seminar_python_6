# Задача : Сумма элементов с нечетными индексами
# def indexes_odd():
#     a = list(map(int, input().split()))
#     nechet=[]
#     
#     for i in range(len(a)):
#         if i%2==1:
#             nechet.append(a[i])
#     print(nechet)
#     print("Сумма элементов с нечетными индексами", sum(nechet))

# indexes_odd()

def indexes_odd():
    a = list(map(int, input().split()))
    print("Сумма элементов с нечетными индексами", sum(list([a[i] for i in range(len(a)) if i%2==1])))

indexes_odd()