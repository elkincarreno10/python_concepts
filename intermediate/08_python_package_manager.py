# Python Package Manager

# PIP http://pypi.org

import numpy

print(numpy.version.version)

numpy_array = numpy.array([32, 45, 56, 76, 32, 23, 45])
print(type(numpy_array))

print(numpy_array * 2)

import pandas

# pip list
# pip uninstall pandas
# pip show numpy

import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(3, 4))


