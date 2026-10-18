import openpyxl


def xlsx_to_txt(xlsx_path, txt_path):
    # Загружаем Excel-файл
    workbook = openpyxl.load_workbook(xlsx_path)

    # Получаем активный лист (можно заменить на workbook['ИмяЛиста'], если нужен конкретный)
    sheet = workbook.active

    # Список для хранения значений непустых ячеек
    values = []

    # Проходим по всем строкам и столбцам листа
    for row in sheet.iter_rows():
        for cell in row:
            # Если ячейка не пустая — добавляем её значение
            if cell.value is not None:
                values.append(str(cell.value))

    # Записываем значения в txt-файл через запятую
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(', '.join(values))

    print(f"Данные успешно записаны в {txt_path}")


# Пример использования
xlsx_file = "/Users/apetrova/Downloads/cpp.xlsx"  # Путь к вашему xlsx-файлу
txt_file = "/Users/apetrova/Downloads/output2.txt"  # Путь к выходному txt-файлу

xlsx_to_txt(xlsx_file, txt_file)