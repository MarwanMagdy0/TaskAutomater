import csv

def read_column_fast(csv_path, column_name):
    result = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            value = row.get(column_name)
            if value is not None:
                result.append(value)
    return result

if __name__ == "__main__":
    numbers = read_column_fast('Numbers\Lebanon Alfa TF01\IMS SMS  My SMS Numbers.csv', 'Number')
    print(numbers)