## @file test_input_handler.py
## @brief Тесты для системы валидации ввода


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from input_handler import InputValidator


## @brief Тест инициализации валидатора
#
# Проверяет корректность инициализации объекта InputValidator.
def test_input_validator_initialization():
    validator = InputValidator(board_size=3)
    assert validator.board_size == 3
    assert validator.validation_log == []
    print(" test_input_validator_initialization passed")


## @brief Тест валидации корректных координат
#
# Проверяет обработку валидных координат на пустом поле.
def test_validate_coordinates_valid():
    validator = InputValidator()
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    is_valid, message = validator.validate_coordinates(0, 0, board)
    assert is_valid == True
    assert "Move is valid" in message
    print(" test_validate_coordinates_valid passed")

## @brief Тест валидации координат вне границ
#
# Проверяет обработку координат, выходящих за границы игрового поля.
def test_validate_coordinates_out_of_bounds():
    validator = InputValidator()
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    is_valid, message = validator.validate_coordinates(5, 5, board)
    assert is_valid == False
    assert "Coordinates must be" in message
    print(" test_validate_coordinates_out_of_bounds passed")

## @brief Тест валидации занятой клетки
#
# Проверяет обработку попытки хода в занятую клетку.
def test_validate_coordinates_occupied():
    validator = InputValidator()
    board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    is_valid, message = validator.validate_coordinates(0, 0, board)
    assert is_valid == False
    assert "Cell is already occupied" in message
    print(" test_validate_coordinates_occupied passed")

## @brief Тест валидации корректного ручного ввода
#
# Проверяет обработку корректного ручного ввода координат.
def test_validate_manual_input_valid():
    validator = InputValidator()
    
    is_valid, row, col, message = validator.validate_manual_input("1", "1")
    assert is_valid == True
    assert row == 0
    assert col == 0
    assert "Coordinates are valid" in message
    print(" test_validate_manual_input_valid passed")

## @brief Тест валидации некорректных чисел
#
# Проверяет обработку нечислового ввода в ручном режиме.
def test_validate_manual_input_invalid_numbers():
    validator = InputValidator()
    
    is_valid, row, col, message = validator.validate_manual_input("abc", "def")
    assert is_valid == False
    assert "Coordinates must be numbers" in message
    print(" test_validate_manual_input_invalid_numbers passed")

## @brief Тест валидации чисел вне диапазона
#
# Проверяет обработку чисел, выходящих за допустимый диапазон.
def test_validate_manual_input_out_of_bounds():
    validator = InputValidator()
    
    is_valid, row, col, message = validator.validate_manual_input("5", "5")
    assert is_valid == False
    assert "Coordinates must be between 1 and 3" in message
    print(" test_validate_manual_input_out_of_bounds passed")

## @brief Тест системы логирования
#
# Проверяет функциональность системы логирования валидатора.
def test_logging_system():
    validator = InputValidator()
    
    validator.log_validation("Тестовое сообщение 1")
    validator.log_validation("Тестовое сообщение 2")
    
    logs = validator.get_recent_logs(2)
    assert len(logs) == 2
    assert "Тестовое сообщение 1" in logs[0]
    assert "Тестовое сообщение 2" in logs[1]
    print(" test_logging_system passed")

## @brief Запуск всех тестов
#
# Выполняет все тесты для системы валидации ввода.
def run_all_tests():
    test_input_validator_initialization()
    test_validate_coordinates_valid()
    test_validate_coordinates_out_of_bounds()
    test_validate_coordinates_occupied()
    test_validate_manual_input_valid()
    test_validate_manual_input_invalid_numbers()
    test_validate_manual_input_out_of_bounds()
    test_logging_system()
    print(" All tests passed successfully!")

## @brief Точка входа для запуска тестов
if __name__ == "__main__":
    run_all_tests()
