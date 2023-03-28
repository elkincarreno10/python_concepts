# Regular Expressions

import re

# match

my_string = 'Esta es la lección número 7: Lección llamada Expresiones Regulares'
my_other_string = 'Esta no es la lección número 6: Manejo de ficheros'

match = re.match('Esta es la lección', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


match = re.match('Esta no es la lección', my_other_string)
if match != None: 
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# search

search = re.search('lección', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall
findall = re.findall('lección', my_string, re.I)
print(findall)


# spplit
split = re.split(':', my_string)
print(split)


# Sub
sub = re.sub('Expresiones Regulares', 'RegEx', my_string)
print(sub)
sub = re.sub('[l|L]ección', 'LECCIÓN', my_string)
print(sub)


# Patterns

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))


pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))


pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))


email = 'elkin@elkindev.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'elkin@elkindev'
print(re.findall(pattern, email))
