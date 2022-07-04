import requests as requests
from random import choice
from BasicWord import BasicWord
import json
import os
from setings import PATCH_DICT_WEB, PATCH_DICT_FILE, PATCH_PLAYER_FILE

def load_random_word():
    """
    Функция получает список слов с внешнего ресурса и
    на основе случайного слова возвращает экземпляр класса BasicWord
    :return:
    """
    try:
        list_word_dict = requests.get(PATCH_DICT_WEB).json()
        with open(PATCH_DICT_FILE, 'w') as file:
            json.dump(list_word_dict, file)
        word = choice(list_word_dict)
    except:
        with open(PATCH_DICT_FILE, encoding='utf-8') as file:
            word = choice(json.load(file))

    return BasicWord(word['word'], word['subwords'])


def write_user_to_file(name, subwords, points):
    """
    Функция записывает данные пользователя в файл
    :return:
    """
    player = dict(user_name=name, user_list_subwords=subwords, user_points=points)
    try:
        #with open(PATCH_PLAYER_FILE, encoding='utf-8') as file:
        #   data = json.load(file)
        #   data.appent(player)
        file = open(PATCH_PLAYER_FILE, encoding='utf-8')
        data = json.load(file)
        data.append(player)
        with open(PATCH_PLAYER_FILE, 'w') as file:
            json.dump(data, file)
    except FileNotFoundError:
        with open(PATCH_PLAYER_FILE, 'w') as file:
            data = []
            data.append(player)
            json.dump(data, file)