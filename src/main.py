"""
@file main.py
 Главный модуль для запуска приложения
"""

from game_board import GameBoard

def main():
    """ Демонстрация базовой структуры
    @return: None
    """

    # Создание и запуск игрового поля
    game_board = GameBoard()
    game_board.run()

if __name__ == "__main__":
    main()