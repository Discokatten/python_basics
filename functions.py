#Write a function full_name(first, last) that returns a full name string.
def full_name(first_name, last_name):
    return f'{first_name} {last_name}'
print(full_name('Sven', 'Göransson'))

#Write a function is_even(number) that returns True if the number is even.
def is_even(number):
    if number % 2 == 0:
        return True
    else: return False
num = int(input('Enter number: '))
print(f'Number is even? {is_even(num)}')

#Write a function sum_list(numbers) that returns the total sum of a list.
def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n

    return total
print(sum_list([1,1,1,1,15]))    

#Write a function max_of_two(a, b) that returns the larger value.
def max_of_two(a, b):
    if a > b:
        return f'{a} is bigger than {b}'
    elif a == b:
        return 'Numbers are the same!'
    elif a < b:
        return f'{b} is bigger than {a}'
num_1 = int(input('Enter number: '))
num_2 = int(input('Enter second number: '))
print(max_of_two(num_1,num_2))

#Write a function to_celsius(fahrenheit) that returns Celsius.
def to_celsius(fahrenheit):
    return (fahrenheit -32 ) * 5/9

temp = int(input('Enter temp: '))
print(f'Temp in C is {round(to_celsius(temp),1)}')

# Create a function grade(score) that returns A, B, C, or F.
def grade(score):
    if score > 50:
        return 'A'
    elif score >= 40:
        return 'B'
    elif score >= 30:
        return 'C'
    else:
        return 'F'

score = int(input("What's your exam score? "))
print(f'Your grade on this exam is {grade(score)}\n')

# Create a function count_vowels(text) that returns how many vowels are in a word.
vowels =  ['a', 'e', 'i', 'o', 'u']
def count_vowels(text):
    count = 0
    for vowel in vowels:
        if vowel in text:
            count += 1
    return count
 
word = input("Count vowels in this word: ")

print(f'{count_vowels(word)} vowel/s in this word \n')

# Create a function safe_divide(a, b) that returns a message if b is 0.
def safe_divide(a,b): 
        if b == 0:
             return '0'
        else: 
            return a//b
        
print('Divide these: ')
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number:  "))
print(f'{num_1} / {num_2} = {safe_divide(num_1, num_2)}')