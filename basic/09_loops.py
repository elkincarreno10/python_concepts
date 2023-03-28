# Loops

# While


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print('Mi condición es mayor o igual que 10')


print('La ejecución continua')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecución')
        break

    print(my_condition)

print('La ejecución continua')

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (22, 1.85, 'Elkin', 'Carreño', 'Elkin')

for element in my_tuple:
    print(element)
    if element == 'Carreño':
        break
    print('Se ejecuta')
else:
    print('El bucle for para la tupla ha terminado')


for element in my_tuple:
    print(element)
    if element == 'Carreño':
        continue
else:
    print('El bucle for para la tupla ha terminado')