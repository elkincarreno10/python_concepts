# Modules

import basic.my_module as my_module

my_module.sumValues(3, 4, 5)
my_module.printValue('Hola Python!')

from basic.my_module import sumValues, printValue

sumValues(5, 2, 4)
printValue('Hello Python!')

import math

print(math.pow(2, 8))

from math import pi as PI_VALUE
print(PI_VALUE)