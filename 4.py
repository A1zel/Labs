import re

# Словарь для преобразования цифр в слова
digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

def number_to_words(num_str):
    return ' '.join(digit_to_word[d] for d in num_str)

def process_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()

    # Разбиваем текст на объекты по пробелам
    objects = text.split()

    result = []
    for i, obj in enumerate(objects, start=1):
        # Проверяем: число ли это (целое), чётное и не длиннее 5 цифр
        if re.fullmatch(r'\d{1,5}', obj):
            num = int(obj)
            if num % 2 == 0 and i % 2 == 1:
                # Чётное число на нечётной позиции — преобразуем в слова
                obj = number_to_words(obj)
        result.append(obj)

    print(' '.join(result))

if __name__ == '__main__':
    process_file('input.txt')