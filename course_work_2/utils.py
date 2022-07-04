import requests as requests
from random import choice
from BasicWord import BasicWord

def load_random_word():
    """
    Функция получает список слов с внешнего ресурса и
    на основе случайного слова возвращает экземпляр класса BasicWord
    :return:
    """
    list_word_dict = requests.get('https://jsonkeeper.com/b/AOXZ').json()
    word = choice(list_word_dict)
    return BasicWord(word['word'], word['subwords'])
