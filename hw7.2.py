def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    line_number = 1
    byte_position = 0
    string_position = dict()
    for i in strings:
        string_position[line_number, byte_position] = f'{i}'
        file.write(f'{i}\n')
        line_number += 1
        byte_position = int(file.tell())
    file.close()
    return string_position



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)