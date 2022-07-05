#from Player import Player
from utils import load_random_word, write_user_to_file, hello_player


def main():
    #player = Player(input("Ввведите имя игрока: "))  # Запрос имений игрока
    player = hello_player()

    # Получаем случайное слово
    word = load_random_word()

    # Приветствуем игрока и предлагаем сыграть
    if player.get_the_number_of_used_word() == 0:
        print(f"Привет, {player.user_name.title()}!\n"
              f"Составьте {len(word.set_subwords)} слов из слова {word.word.upper()}\n"
              f"Слова должны быть не короче 3 букв\n"
              f"Чтобы закончить игру, угадайте все слова или напишите 'stop' или 'стоп'\n"
              f"Поехали, ваше первое слово?\n"
             )
    else:
        print(f"С возвращением, {player.user_name.title()}!\n"
              f"У вас {player.get_points()} очков. Продолжим\n"
              f"Составьте {len(word.set_subwords)} слов из слова {word.word.upper()}\n"              
              f"Поехали, ваше первое слово?\n"
              )


    # Цикл ввода слов пользователем

    while player.get_the_number_of_used_word() != word.counting_subwords():
        user_answer = input('>: ')
        if user_answer in ['стоп', 'stop']:
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
            print(f"""Верно! Вы заработали 10 очков Ещё {word.counting_subwords() - player.get_the_number_of_used_word()} слов""")

    # Вывод результата игры
    print(f"""Игра завершена, вы угадали {player.get_the_number_of_used_word()} слов и заработали {player.get_points()} очков!""")

    # Заносим данные пользователя в файл
    write_user_to_file(player.get_name(), player.get_user_subwords(), player.get_points())


if __name__ == '__main__':
    main()
