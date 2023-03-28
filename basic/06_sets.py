# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario


my_other_set = {'Elkin', 'carreño', 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('ElkinDev')
print(my_other_set) # Un set no es un estructura ordenada

my_other_set.add('ElkinDev')
print(my_other_set) # Un set no admite repetidos

print('Elkin' in my_other_set)
print('Moure' in my_other_set)

my_other_set.remove('Elkin')
print(my_other_set)


my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) No está definido porque lo eliminamos

my_set = {'Elkin', 'carreño', 22}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Javascript', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)


print(my_new_set.difference(my_set))