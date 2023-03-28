# Functions

def my_funciton():
    print('Esto es una función')

my_funciton()
my_funciton()


def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(3, 6)
sum_two_values(353245, 654325)
sum_two_values('3', '6')
sum_two_values(3.1, 6.2)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname = 'Carreño', name = 'Elkin')

def print_name_with_default(name, surname, alias = 'Sin Alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Elkin', 'Carreño')
print_name_with_default('Elkin', 'Carreño', 'ElkinDev')


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'Python', 'ElkinDev')
print_upper_texts('Hola')
