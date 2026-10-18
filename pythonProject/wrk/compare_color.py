import datetime
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# Сравнивает значения из стобца А на Листе2 со значениями из столбца А на Листе1.
# При совпадении окрашивает ячейку из столбца B, находящуюся в том же ряду, в красный цвет

file_path = '/Users/apetrova/Downloads/compare_color.xlsx'
current_date = datetime.datetime.now().strftime('%H.%M.%S')

# Загрузка книги
wb = load_workbook(file_path)

# Получение листов
sheet1 = wb['DependsON']
sheet2 = wb['Лист1']
sheet3 = wb['DependsBY']
sheet4 = wb['Лист2']

# Определение заливки ячеек
red_fill = PatternFill(start_color='FF8E92', end_color='FF8E92', fill_type='solid')

# Составление набора со значениями из колонки А на Листе1
values_sheet2 = set()
for row in sheet2.iter_rows(min_row=1, max_col=1, max_row=sheet2.max_row):
    cell = row[0]
    if cell.value is not None:
        values_sheet2.add(str(cell.value).strip())

for row in sheet1.iter_rows(min_row=1, max_col=2, max_row=sheet1.max_row):
    cell_a = row[0]  # ячейка в столбце A
    cell_b = row[1]  # ячейка в столбце B

    # Если значение из спиcка с Листа1 есть в ячейке в столбце А на Листе DependsON, происходит окрашивание
    if cell_a.value is not None:
        if str(cell_a.value).strip() in values_sheet2:
            #cell_b.fill = red_fill
            cell_b.value = '35'

# Составление набора со значениями из колонки А на Листе2
values_sheet4 = set()
for row in sheet4.iter_rows(min_row=1, max_col=1, max_row=sheet4.max_row):
    cell = row[0]
    if cell.value is not None:
        values_sheet4.add(str(cell.value).strip())

for row in sheet3.iter_rows(min_row=1, max_col=2, max_row=sheet3.max_row):
    cell_a = row[0]  # ячейка в столбце A
    cell_b = row[1]  # ячейка в столбце B

    # Если значение из спиcка с Листа2 есть в ячейке в столбце А на Листе DependsBY, происходит окрашивание
    if cell_a.value is not None:
        if str(cell_a.value).strip() in values_sheet4:
            #cell_b.fill = red_fill
            cell_b.value = '35'

wb.save(file_path)
print(f"{current_date} Обработка завершена. Файл сохранён")