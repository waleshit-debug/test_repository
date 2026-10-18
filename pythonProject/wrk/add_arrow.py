import openpyxl
from openpyxl import load_workbook, workbook
import os


# Если ячейка в файле содержит число, ставит символ ↑ или ← перед этим числом

def add_arrow(file_path):
    workbook = openpyxl.load_workbook(file_path)

    # Индикация работы на каждом листе
    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        print(f"\nОбработка листа: {sheet_name}")

        # Создание спика ячеек для обработки
        cells_to_process = list(sheet.iter_rows())
        cells_modified = 0
        arrow = '← '

        for row in cells_to_process:
            for cell in row:
                # Проверка на наличе числа в ячейке
                if isinstance(cell.value, int):
                    cell.value = str(arrow) + str(cell.value)  # вставка символа
                    cells_modified += 1
                    continue

        if cells_modified > 0:
            print(f"На листе '{sheet_name}' изменено {cells_modified} ячеек (обработка .cpp)")

        workbook.save(file_path)
        print("Обработка завершена. Файл сохранён")


file_path = '/Users/apetrova/Downloads/add_arrow.xlsx'
add_arrow(file_path)
