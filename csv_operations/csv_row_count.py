import csv

# Replace 'file.csv' with your CSV file path
file_path = 'D:/Study Material/Data_Management/GoalA/DataManagement_GoalA.csv'
# file_path = 'D:/Study Material/Data_Management/GoalA/DBtrainrides.csv'

# Open the CSV file and count the number of rows
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    row_count = sum(1 for row in csv_reader)

print(f'Total number of rows: {row_count}')
