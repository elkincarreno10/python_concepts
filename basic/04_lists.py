# Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]


print(my_list)
print(len(my_list))

my_other_list = [22, 1.85, 'Elkin', 'Carreño']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(62))

print('====')
age, heigth, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append('ElkinDev')
print(my_other_list)

my_other_list.insert(1, 'Rojo')
print(my_other_list)

my_other_list[1] = 'Negro' 

my_other_list.remove('Negro')
print(my_other_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = 'Hola Python'
print(my_list)