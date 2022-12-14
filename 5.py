# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# N = int(input(" для N --> "))
# formula = {}
# for i in range(1, N+1):
#     formula [i]= round((1 + 1/N)**N ,3)

# print (formula)

n = int(input(" для N --> "))
formula = {round((1 + 1/n)**n ,3) for n in range(1, n+1)}
from functools import reduce
print (formula,"Сумма элементов: ",reduce((lambda x,y:x+y), list(formula)))