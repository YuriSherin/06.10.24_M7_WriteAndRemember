def custom_write(file_name, strings):
    """Функция принимает аргументы file_name - название файла для записи, strings - список строк для записи
    Функция записывает в файл file_name все строки из списка strings, каждая на новой строке
    и возвращает словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка"""
    strings_positions = {}          # словарь
    num_str = 1     # номер записываемой строки, начинается с 1
    num_tell = 0    # позиция файлового указателя относительно начала файла

    try:        # обработка исключений
        with open(file_name, 'w', encoding='utf8') as file:
            for line in strings:
                num_tell = file.tell()          # получим позицию файлового указателя
                strings_positions[(num_str, num_tell)] = line   # добавим данные в словарь
                file.write(line + '\n')         # сохраним данные в файл
                num_str += 1                    # увеличим номер обрабатываемой строки
    except OSError as e:
        print(f'Ошибка записи данных в файл: {e}')
    return  strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)

    for elem in result.items():
        print(elem)
