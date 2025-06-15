def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден!")
        return ""
def is_valid_number(number):
    # Проверяем, что число четное
    if int(number) % 2 != 0:
        return False
    # Проверяем, что число не более 5 цифр
    if len(number) > 5:
        return False
    return True
def convert_number_to_words(number):
    # Словарь для замены цифр на слова
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
    result =
    for digit in number:
        result.append(digit_to_word.get(digit, digit))
    return ' '.join(result)
def process_file(filename):
    content = read_file(filename)
    if not content:
        return
    # Разделяем содержимое по пробелам
    tokens = content.split()
    # Счетчик для определения позиции числа
    position = 1
    for token in tokens:
        if token.isdigit() and is_valid_number(token):
            if position % 2 == 1:  # Нечетная позиция
                print(f"Исходное число: {token}")
                print(f"Преобразованное число: {convert_number_to_words(token)}")
            else:
                print(f"Число на четной позиции: {token}")
            print("-" * 30)
        position += 1
if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    process_file(filename)