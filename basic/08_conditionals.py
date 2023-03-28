# Conditionals

my_condition = False

if my_condition:
    print('Se ejecuta la condición del if')

my_condition = 25

if my_condition == 10:
    print('Se ejecuta la condición del segundo if')

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_condition == 25: 
    print('Es igual que 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20')

print('La ejecución continuó')
