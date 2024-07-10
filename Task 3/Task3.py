import json
import sys


def report_values(test_items):
    for item in test_items:
        if item['id'] in Values_dict:
            item['value'] = Values_dict[item['id']]
        if 'values' in item:
            report_values(item['values'])


with open(sys.argv[1], 'r', encoding='utf-8') as f:
    Values_data = json.load(f)

with open(sys.argv[2], 'r', encoding='utf-8') as f:
    Tests_data = json.load(f)

# Создание словаря для быстрого поиска значений по id
Values_dict = {item['id']: item['value'] for item in Values_data['values']}

report_values(Tests_data['tests'])

with open(sys.argv[3], 'w+', encoding='utf-8') as f:
    json.dump(Tests_data, f, indent=4)
