"""
@file main.py
@brief Главный модуль для запуска приложения
"""

from game_board import GameBoard

def main():
    """
    @brief Запуск PITIC-1 - демонстрация базовой структуры
    @return: None
    """

    # Создание и запуск игрового поля
    game_board = GameBoard()
    game_board.run()

if __name__ == "__main__":
    main()