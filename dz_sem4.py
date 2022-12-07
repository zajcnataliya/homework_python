# 1'. Вычислить число Пи c заданной точностью d (метод math.pi возвращает значение pi)
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

print()
print('Задача 1, способ 1')

from math import pi

d = int(input('Введите число для заданной точности числа Пи: '))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# print()
# print('Задача 1, способ 2')

# def format_by_mask(num: float, accuracy: float) -> float:
#     """форматирует число по заданной маске"""
#     accuracy = str(accuracy)
#     accuracy = len(accuracy[accuracy.find('.')+1::])
#     return float(f'{pi:0.{accuracy}f}')

# d = input('Введите точность в формате "0.0001": ')    
# print(format_by_mask(pi, d))

# 2'. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
# * 6 -> [2,3] встречается 1 раз
# * 144 -> [2,3] встречается 4 раз - 2 и 2 раза - 3

print()
print('Задача 2, способ 1')

n = int(input('Введите число: '))
i = 2 # первое простое число
list = []
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f'Простые множители: {list}')


print()
print('Задача 2, способ 2')

def dividers(n: int, uniq: bool = False): #-> list[int]:
    """Возвращает список простых делителей числа.
    uniq = True вернет список уникальных делителей"""
    i = 2
    dividers = []
    while n != 1:
        while n % i == 0:
            dividers.append(i)
            n //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers     

n = 81
print(f'Список натуральных делителей числа {n}:{dividers(n)}') 
print(f'Список уникальных делителей числа {n}:{dividers(n, True)}')

# 3'. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

print()
print('Задача 3, способ 1')

list1 = input('Введите числа через пробел: ').split()
print(f'Исходный список: {list1}')
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(f"Список из неповторяющихся элементов: {list2}")

print()
print('Задача 3, способ 2')

from random import randint as rnd
mass = [rnd(1, 7) for i in range(12)]
print(f'исходный список: {mass}')
print(f'Cписок уникальных элементов: {list(set(mass))}')
mass = [i for i in mass if mass.count(i) ==1]
print(f'Uniq: {mass}')



# 4'. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5
# random randint

print()
print('Задача 4')

import sympy
from random import randint as rnd

def create_polinom(k: int, simple: bool = True) -> str:
    """Генерирует полином со случайными коэффициентами степени K
    simple = False вернет полином без сокращения нулевых коэффициентов"""
    polinom = ''
    for i in range (k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)            

def create_pol_file(polinom: str, filename: str = 'new'):
    """Записывает полином в файл, дополнительно можно указать имя файла"""
    with open(f'Seminars_Python/{filename}.txt', 'w') as f:
        f.write(polinom)

k = int(input())
print(f'Сгенерированный полином {create_polinom(k)}')
print(f'Сгенерированный полином {create_polinom(k, False)}')
create_pol_file(create_polinom(k))


# 5'. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

print()
print('Задача 5')

from sympy import simplify

degree = int(input('Задайте степень: '))

pol1 = create_polinom(degree)    # генерируем полином
pol2 = create_polinom(degree)

filename1 = 'first'
filename2 = 'second'
sum_filename = 'sum'

create_pol_file(pol1, filename1) # создаем файлы с полиномами
create_pol_file(pol2, filename2)

with open(f'Seminars_Python/{filename1}.txt', 'r') as f1: #считываем из файла информацию
    f_pol = f1.read()
    print(f'Первый полином: {f_pol}')

with open(f'Seminars_Python/{filename2}.txt', 'r') as f2:
    s_pol = f2.read()
    print(f'Второй полином: {s_pol}')

sum_of_pols = simplify(f_pol + '+' + s_pol)   #складываем полиномы
sum_of_pols = str(sum_of_pols)

with open(f'Seminars_Python/{sum_filename}.txt', 'w') as s: #считываем из файла информацию
    s.write(sum_of_pols)
    print(f'Сумма полиномов: {sum_of_pols}')