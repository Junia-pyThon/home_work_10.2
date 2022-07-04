from Player import Player
from utils import load_random_word


def main():
    name = input("Ввведите имя игрока: ")  # Запрос имений игрока

    player = Player(name)  # Создание экземпляра класса

    word = load_random_word()  # Получаем случайное слово

    # Приветствуем игрока и предлагаем сыграть
    print(f"Привет, {player.user_name.title()}!\n"
          f"Составьте {len(word.set_subwords)} слов из слова {word.word.upper()}\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите 'stop' или 'стоп'\n"
          f"Поехали, ваше первое слово?\n"
          )

    # Цикл ввода слов пользователем
    while player.get_the_number_of_used_word() != word.counting_subwords():
        user_answer = input('>: ')
        # Проверяем не желает ли пользователь прекратить игру
        match user_answer:
            case 'стоп':
                break
            case 'stop':
                break
        if len(user_answer) < 3:  # Смотрим не короткое ли слово
            print("Слишком короткое слово")
        elif not word.checking_word_of_subwords(user_answer):  # Допустимо ли слово
            print("Неверно")
        elif player.checking_use_word_before(user_answer):  # Проверяем вугадал ли пользователь ранее это слово
            print("Уже использовано")
        else:
            # Добавляем слово в список угаданных
            player.added_word_in_subwords(user_answer)
            # Присваиваем очки
            player.points_up()
            # Оповещаем пользователя
            print(f"""Верно! Вы заработали 10 очков 
                      Ещё {word.counting_subwords() - player.get_the_number_of_used_word()} слов""")

    # Вывод результата игры
    print(f"""Игра завершена, вы угадали {player.get_the_number_of_used_word()} слов
              и заработали {player.get_points()} очков!""")


if __name__ == '__main__':
    main()
