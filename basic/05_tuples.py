# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.85, 'Elkin', 'Carreño', 'Elkin')
my_other_tuple = (35, 60, 30)

print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Elkin'))
print(my_tuple.index('Carreño'))
print(my_tuple.index('Elkin'))

# my_tuple[1] = 1.80 Error
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'ElkinDev'
my_tuple.insert(1, 'Negro')

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) Eror, no está definida

