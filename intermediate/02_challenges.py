# Challenges

# Múltiplos de 3 y 5-Fizz-Buzz 3-Fizz 5-Buzz 
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} - FIZZ-BUZZ!!!')
        elif i % 3 == 0:
            print(f'{i} - Fizz')
        elif i % 5 == 0:
            print(f'{i} - Buzz')
        else:
            print(f'{i}')
fizz_buzz()

# Anagrama
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram('Amor', 'Roma'))

# Sucesión de Fibonacci
def fibonacci():
    fibonacci_list = []
    for i in range(0, 50):
        if i == 0 or i == 1:
            print(i)
            fibonacci_list.append(i)
        else:
            print(fibonacci_list[-1] + fibonacci_list[-2])
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

fibonacci()

# Es un número primo
def is_prime():
    for number in range(1, 101):
        if number >= 2:

            is_divisible = False

            for i in range(2, number):
                if number % i == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_prime()

# Invirtiendo cadenas

def reverse(text):

    text_len = len(text)
    reverse_text = ''

    for index in range(0, text_len):
        reverse_text += text[text_len - index - 1]

    return reverse_text

print(reverse('Hola mundo'))

