import requests as requests
from random import choice
from BasicWord import BasicWord
import json
from setings import PATCH_DICT_WEB, PATCH_DICT_FILE

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
