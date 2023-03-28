# Exception Handling

number_one = 5
number_two = 1
number_two = '1'

# Try except
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except: 
    # Se ejecuta si se produce una excepción
    print('Se ha producido un error')


# Try except else
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except: 
    print('Se ha producido un error')
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print('La ejecución continua correctamente')
finally: # Opcional
    # Se ejecuta siempre
    print('La ejecución continua')


# Exceptiones por tipo
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError: 
    # Se ejecuta si se produce una excepción
    print('Se ha producido un error')
except TypeError: 
    # Se ejecuta si se produce una excepción
    print('Se ha producido un error')

# Captura de la información de la excepción
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
