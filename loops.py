# Menu loop: show choices until user selects q to quit.
# Input validation: keep asking until input is valid.
# Retry logic: ask for password again until it is correct.

# Use a for loop to print numbers from 1 to 10.
numbers = [1,2,3,4,5,6,7,8,9,10]
for n in numbers:
    print(n)

# Use a loop to find the sum of [4, 9, 2, 5].
numbers = [4, 9, 2, 5]
total = 0
for n in numbers:
  total = total + n
print(f'The sum of {numbers} is {total}')

# Use a while loop to print numbers from 10 down to 1.
numbers = [1,2,3,4,5,6,7,8,9,10]
count = 11
while count > 0:
   numbers.reverse()
   print(numbers)
   count =- 1

# Ask the user for a positive number. Keep asking until they enter a valid value.
number = int(input('Enter a positive number: '))
while number < 0:
    number = int(input('Try again: '))
    
print('YES! Positive number!')

# Count how many even numbers are in [3, 8, 11, 14, 20].
numbers = [3, 8, 11, 14, 20]
total = 0
for n in numbers:
   if n / 2 == 0:
       total += 1
       print(f'{total} even numbers in {numbers}')

# Print each letter of a word using a loop.
word = input('Enter a word: ')
for char in word:
   print(char)


# Print the multiplication table for a number chosen by the user.
num = int(input('Enter a number to show multiplication table: '))
for i in range(1,11):
   print(num, 'x', i, '=', num*i) 

#Ask for five numbers and print the largest number entered.
highest_num = int(input('Enter a number: '))
for i in range(4):
    num = int(input('Enter another number: '))
    if num > highest_num:
        highest_num = num

print("The highest of your numbers are:", highest_num)

#Use a loop to count how many even numbers are in a list.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print(f'{count} even numbers in {numbers}')