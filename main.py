KEY_CODE = "-e"
KEY_DE_CODE = "-d"
KEY_STRING = "-s"
FIND_STRING = " -s"

def init_alphabet():
    alphabets = []
    alphabets.append("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")  # переменная содержащая русский алфавит
    alphabets.append("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    alphabets.append("abcdefghijklmnopqrstuvwxyz")
    alphabets.append(".,';:\\|*-+=/")
    alphabets.append(("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    alphabets.append("0123456789")

    return alphabets

def get_alphabet(alphabets, symbol):
    for alphabet in alphabets:
        if symbol in alphabet:
            return alphabet

def processing_string():
    user_value = input("Введите что-нибудь здесь")  # переменная строки которую вводит пользователь
    string_of_operation = cutout_string(user_value)

    if is_code_string_res(user_value):
        return code_string(string_of_operation)
    else:
        return de_code_string(string_of_operation)

def is_code_string_res(user_value):
    if user_value.startswith(KEY_DE_CODE) and KEY_STRING in user_value:
        return False
    else:
        return True

def cutout_string(user_value):
    if KEY_STRING in user_value and (KEY_CODE in user_value or KEY_DE_CODE in user_value):
        index = user_value.find(FIND_STRING)
        return user_value[index + len(FIND_STRING):len(user_value)]
    else:
        return user_value

def code_string(user_value): #вызывается функция
    alphabets = init_alphabet()
    new_string = "" #переменная закодированной строки
    for i in user_value: #цикл
        index = -1  # переменная индекс
        use_alphabet = get_alphabet(alphabets, i)
        if use_alphabet is not None:
            index = use_alphabet.index(i) + 5
            if index > len(use_alphabet):  # условие если измененный индекс стал больше 33
                index -= len(use_alphabet)  # вычитаем из большего числа 33
        if index == -1:
            new_string += i
        else:
            new_string += use_alphabet[index]  # кпеременной "новая строка" добавляется новый символ

    return new_string

def de_code_string(user_value):
    alphabets = init_alphabet()
    new_string = ""  # переменная закодированной строки
    for i in user_value:  # цикл
        index = -1  # переменная индекс
        use_alphabet = get_alphabet(alphabets, i)
        if use_alphabet is not None:
            index = use_alphabet.index(i) - 5
            if index < 5:  # условие если измененный индекс стал больше 33
                index -= 5 + len(use_alphabet)  # вычитаем из большего числа 33
        if index == -1:
            new_string += i
        else:
            new_string += use_alphabet[index]  # кпеременной "новая строка" добавляется новый символ

    return new_string


print(processing_string()) #напечатай новую строку