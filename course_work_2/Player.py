class Player:
    def __init__(self, name, points=0):
        self.user_name = name
        self.user_list_subwords = []
        self.user_points = points

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

    def points_up(self):
        """
        Добавляем очки пользователю
        """
        self.user_points += 10

    def get_points(self):
        """
        Возвращаем кол-во заработаных очков
        """
        return self.user_points


