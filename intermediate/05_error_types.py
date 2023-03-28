# Error Types

# SyntaxError
# print 'Hola comunidad!' # Error
print('Hola comunidad!')

# NameError
language = 'Spanish'
print(language)

# IndexError
my_list = ['Python', 'Swift', 'Kotiln', 'Dart', 'Javascript']
print(my_list[4])
# print(my_list[5])

# ModuleNotFoundError
# import maths
import math

# AttributeError
# print(math.PI) 
print(math.pi)

# KeyError
my_dict = {'Nombre': 'Elkin', 'Apellido': 'Carreño', 'Edad': 22, 1:'Python'}
print(my_dict['Nombre'])
# print(my_dict['Nombr'])

# TypeError
# print(my_list['0'])
print(my_list[0])


# ImportError
# from math import PI
from math import pi
print(pi)


# ValueError
# my_int = int('10 Años')
my_int = int('10')
print(type(my_int))

# ZeroDivisionError
# print(4/0)
print(4/2)


