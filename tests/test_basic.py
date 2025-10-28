## @file test_basic.py
## @brief Базовые тесты для проекта

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


## @brief Тест импортов основных модулей
#
# Проверяет корректность импорта всех основных модулей проекта.
#
# @return True если все импорты работают корректно, иначе False
def test_imports():
    try:
        from input_handler import InputValidator
        from game_board import GameBoard
        print("All imports are working correctly")
        return True
    except ImportError as e:
        print(f"Error import: {e}")
        return False


## @brief Тест базового синтаксиса Python
#
# Проверяет базовый синтаксис Python на корректность.
#
# @return True если синтаксис корректен, иначе False
def test_basic_syntax():
    try:
        # Простая проверка синтаксиса
        x = 1 + 1
        assert x == 2
        print("Python's basic syntax is correct")
        return True
    except Exception as e:
        print(f"Error syntax: {e}")
        return False

## @brief Главная функция запуска тестов
#
# Запускает все базовые тесты и возвращает код завершения.
if __name__ == "__main__":
    success = test_imports() and test_basic_syntax()
    if success:
        print("Basic tests passed!")
    else:
        print("Basic tests failed!")
        sys.exit(1)
