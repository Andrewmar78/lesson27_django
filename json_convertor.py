import csv
import json

CSV_PATH_1 = 'datasets/ads.csv'
CSV_PATH_2 = 'datasets/categories.csv'
JSON_PATH_1 = 'datasets/ads.json'
JSON_PATH_2 = 'datasets/categories.json'


def csv_to_json(csv_file, json_file):
    json_list = []

    with open(csv_file, encoding="utf-8") as file:
        for row in csv.DictReader(file):
            json_list.append(row)
            # print(row)

    with open(json_file, 'w', encoding="utf-8") as outfile:
        outfile.write(json.dumps(json_list, ensure_ascii=False, indent=4))


csv_to_json(CSV_PATH_1, JSON_PATH_1)
csv_to_json(CSV_PATH_2, JSON_PATH_2)
