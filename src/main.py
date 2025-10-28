## @file main.py
## @brief Главный модуль для запуска приложения крестики-нолики


from game_board import GameBoard
## @brief Главная функция приложения
#
# Создает экземпляр игрового поля и запускает главный цикл
# обработки событий Tkinter.
#
# @return None
def main():
    # Создание и запуск игрового поля
    game_board = GameBoard()
    game_board.run()

## @brief Точка входа в программу
if __name__ == "__main__":
    main()
