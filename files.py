from pathlib import Path
import csv
import json

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
TXT_FILE = DATA_DIR / 'data.txt'
STUDENTS_FILE = DATA_DIR / 'students.csv'
CONFIG_FILE = DATA_DIR / 'config.json'

ENCODING = 'utf-8'
# Create txt file with two lines
# Write Python code to read and print all content.
# Write Python code that appends this line to notes.txt: I can append!
with open(DATA_DIR / 'data.txt','w', encoding=ENCODING) as file:
    file.write('This is a text-file \n')

try:
    with open(TXT_FILE, 'r', encoding=ENCODING) as file:
        print( file.read())
except FileNotFoundError:
    print('File not found.')

with open(TXT_FILE, 'a', encoding=ENCODING) as file:
    print(file.write('I can append! \n'))

# Write Python code to read students.csv and print each name and score.
# Create a list of two dictionaries and write it to results.csv.
with open(STUDENTS_FILE, 'r', encoding=ENCODING) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'name: {row['name']}, score:{ row['score']}')

data = [{'name':'Helge', 'score': '13'},
        {'name':'Stig', 'score':'143' }]

with open(DATA_DIR / 'results.csv', 'w', newline='', encoding=ENCODING) as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'score'])
    writer.writeheader()
    writer.writerows(data)

# Write Python code to load config.json and print course and week.
with open(CONFIG_FILE, 'r', encoding=ENCODING) as file:
    data = json.load(file)
    print(f'Course: {data['course']}, week: {data['week']}')


# Save a dictionary to summary.json with json.dump.
data = [{'course':'dans', 'score':'17'}, {'course':'bamsegympa','score':'145'}]
with open(DATA_DIR / 'summary.json', 'w', encoding=ENCODING) as file:
    json.dump(data, file)

with open(DATA_DIR / 'summary.json' ,'r', encoding=ENCODING) as file:
    data = json.load(file)
for courses in data:
    print(f'Added course: {courses['course']}')

# Create inventory_notes.txt and write two short lines about your inventory task.
with open(DATA_DIR / 'inventory_notes.txt', 'w', encoding=ENCODING) as file:
    file.write('Hello, this is an inventory-task')

# Append one extra line to inventory_notes.txt.
with open(DATA_DIR / 'inventory_notes.txt', 'a', encoding=ENCODING) as file:
    file.write('This is another line!')


# Create inventory.csv with this content:
# item,quantity
# Pen,10
# Book,5
# Bag,12
with open(DATA_DIR / 'inventory.csv', 'w', newline='', encoding=ENCODING) as file:
    data = [{'item':'Pen', 'quantity': '10'},
            {'item':'Book', 'quantity': '5'},
            {'item':'Bag', 'quantity': '12'}]
    writer = csv.DictWriter(file, fieldnames=['item', 'quantity'])
    writer.writeheader()
    writer.writerows(data)

# Read the CSV and calculate the total quantity.
with open(DATA_DIR / 'inventory.csv', 'r', encoding=ENCODING) as file:
    data = csv.DictReader(file)
    total = 0
    for post in data:
        total += int(post['quantity'])
    print(f'Total inventory: {total}')

# Save the result into inventory_summary.json as {"total_quantity": ...}.
# Print the JSON value after reading it back.
with open(DATA_DIR / 'inventory_summary.json', 'w', encoding=ENCODING) as file:
    data = {'total_quantity':total}
    json.dump(data, file)
with open(DATA_DIR / 'inventory_summary.json', 'r', encoding=ENCODING) as file:
    data = json.load(file)
    print(data)