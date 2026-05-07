# if-statement conditions end with :
# indentation after if and elif instead of else if
# python uses and/or as logical operators

# Ask for temperature and print Cold, Warm, or Hot.
temp = int(input('Enter temp: '))
if temp > 20:
   print('Temperature is hot')
elif temp >= 12:
   print('Temperature is warm')
else:
   print('Temperature is cold')

# Ask for a number and print whether it is even or odd.
nr = int(input('Enter a number: '))
if nr % 2 == 0:
   print('The number you entered is even')
else:
   print('The number you entered is odd')

# Ask for username and password and print Login success only if both are correct.
user_name = input('Enter username: ')
pwd = input('Enter password: ')
user_name_correct = user_name == True
pwd_correct = pwd == True

if user_name_correct and pwd_correct:
   print('Login successful')
else:
   print('Check credentials')

# Ask for age and print whether the user can vote (18 or older).
age = int(input('Enter your age: '))
voting_age = 18
if age >= voting_age:
   print("You're allowed to vote!")
else:
   print("You're not an adult")

# Ask for exam score and print grade level (A, B, C, F) using simple ranges.
score = int(input("What's your exam score? "))
if score > 50:
   print('Your grade on this exam is A')
elif score >= 40:
   print('Your grade on this exam is B')
elif score >= 30:
   print('Your grade on this exam is C')
else:
   print('Your grade on this exam is F')

# Ask for two numbers and print which one is larger. If equal, print Same value.
num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
if num_1 > num_2:
   print('First number is larger than the second')
elif num_1 == num_2:
   print('Same value')
elif num_1 < num_2:
   print('Second number is larger than the first')
else:
   print('Something went wrong')

#Build a small grade checker for scores from 0 to 100.
score = int(input("What's your exam score? "))
score_in_range = 0 < score < 100
if not score_in_range:
   print("You've entered an invalid score")
elif score >= 70 :
   print('Your grade on this exam is A')
elif score >= 50:
   print('Your grade on this exam is B')
elif score >= 30:
   print('Your grade on this exam is C')
else:
   print('Your grade on this exam is F')


#Ask for three numbers and print the largest.
num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
num_3 = float(input('Enter third number: '))
if  num_3 < num_1 and num_2 < num_1:
   print('First number is the largest')
elif num_1 < num_2 and num_3 < num_2:
   print('Second number is the largest')
elif num_1 == num_2 == num_3:
   print('All numbers have the same value')
elif num_1 < num_3 and num_2 < num_3 :
   print('Third number is the largest')
else:
   print('Something went wrong')

#Ask for a year and print whether it is a leap year (basic rule only: divisible by 4).
year = int(input('Enter year: '))
leap_year = year % 4 == 0                                                   
if leap_year:
    print('This is a leap year')
else:
    print('Not a leap year')