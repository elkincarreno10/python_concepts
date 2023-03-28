# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre': 'Elkin', 'Apellido': 'Carreño', 'Edad': 22, 1:'Python'}
my_dict = {
    'Nombre': 'Elkin', 
    'Apellido': 'Carreño', 
    'Edad': 22, 
    'Lenguajes':{'Python', 'Swift', 'Kodin'},
    1:1.85
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Brais'
print(my_dict)


print(my_dict[1])

my_dict['calle'] = 'Calle ElkinDev'
print(my_dict)

del my_dict['calle']
print(my_dict)


print('Carreño' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre', 1, 'Piso']

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, 'Elkin')
print(my_new_dict)

print(my_new_dict.values())


