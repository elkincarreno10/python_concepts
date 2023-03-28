# Classes

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} ({alias})' # Propiedad Pública
        self.__name = name # Propiedad Privada

    def get_name (self):
        return self.__name

    def walk(self):
        print(f'{self.full_name} Está caminando')

my_person = Person('Elkin', 'Carreño')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('Fabian', 'Coronel', 'FabianDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Héctor de León (El loco de los perros)'
print(my_other_person.full_name)


my_other_person.full_name = 1234
print(my_other_person.full_name)