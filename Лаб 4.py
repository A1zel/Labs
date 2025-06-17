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

def is_even_number(s):
    # Проверяем, что строка - число, чётное и не длиннее 5 символов
    if not s.isdigit():
        return False
    if len(s) > 5:
        return False
    num = int(s)
    return num % 2 == 0

def number_to_words(num_str):
    return ' '.join(digit_to_word[d] for d in num_str)

def main():
    text = input("Введите числа через пробел: ")

    objects = text.split()

    even_numbers = [obj for obj in objects if is_even_number(obj)]

    for idx, number in enumerate(even_numbers, start=1):
        if idx % 2 == 1:  # нечетная позиция
            print(number_to_words(number))
        else:
            print(number)

if __name__ == "__main__":
    main()