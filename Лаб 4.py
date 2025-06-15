import re

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

def number_to_prose(number_str):
    return ''.join(digit_to_word[d] for d in number_str)


def process_text(text):
    pattern = re.compile(r'\d+')

    def replace_match(match):
        num_str = match.group()
        return number_to_prose(num_str)

    result = pattern.sub(replace_match, text)
    return result

def main():
    filename = input("Введите имя файла: ")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return

    objects = text.split()

    processed_objects = []
    for obj in objects:
        if re.fullmatch(r'\d+', obj):
            processed_objects.append(number_to_prose(obj))
        else:
            processed_objects.append(obj)

    # Выводим результат
    print('Обработанный текст:')
    print(' '.join(processed_objects))

if __name__ == "__main__":
    main()