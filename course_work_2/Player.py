class Player:
    def __init__(self, name):
        self.user_name = name
        self.user_list_subwords = []

    def __repr__(self):
        return f"Экземпляр класса Player, содержащий в себе имя пользователя и список используемых им слов"

    def get_the_number_of_used_word(self) -> int:
        """Возвращает кол-во использованых пользователем слов"""
        return len(self.user_list_subwords)

    def added_word_in_subwords(self, word: str):
        """Добавляет слово в список"""
        self.user_list_subwords.append(word)

    def checking_use_word_before(self, word):
        """Проверяет использовалось ли слово ранее"""
        if word in self.user_list_subwords:
            return True
        else:
            return False

