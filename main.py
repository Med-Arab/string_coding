def init_alphabet():
    alphabets = []
    alphabets.append("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")  # переменная содержащая русский алфавит
    alphabets.append("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    alphabets.append("abcdefghijklmnopqrstuvwxyz")
    alphabets.append(".,';:\\|*-+=/")

    return alphabets


def get_alphabet(alphabets, symbol):
    for alphabet in alphabets:
        if symbol in alphabet:
            return alphabet


def code_string(): #вызывается функция
    user_value = input("Введите что-нибудь здесь") #переменная строки которую вводит пользователь
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


print(code_string()) #напечатай новую строку