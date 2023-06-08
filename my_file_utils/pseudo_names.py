# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randrange

def pseudo_names():
    """
    Генерируем псевдо-имя для файла
    :return: имя файла
    """
    all_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowel_alphabet = 'aeiou'
    ret = "qwe"
    ret = ret.capitalize()
    return ret
