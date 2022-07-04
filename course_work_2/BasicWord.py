class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.set_subwords = set(subwords)

    def __repr__(self):
        return f"Экземпляр класса BasicWord, содержащий базовое слово {self.word}",\
               f"и список слов {self.set_subwords}, которые можно сотсавить из его букв"

    def checking_word_of_subwords(self, user_word):
        """Проверяет находится ли слово в списке допустимых"""
        return user_word in self.set_subwords

    def counting_subwords(self):
        """Возвращает кол-во использованых слов"""
        return len(self.set_subwords)
