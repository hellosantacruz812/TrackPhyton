# TODO импортировать необходимые молули
import json
import csv
from xml.etree.ElementTree import indent

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        line = [lines for lines in csv.DictReader(f)]  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(line,f, indent=4)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
