## @file input_handler.py
## @brief Система ввода и валидации ходов игрока


## @brief Класс для валидации ввода игрока
#
# Осуществляет проверку координат на соответствие границам поля
# и доступность клеток для хода.
class InputValidator:

    ## @brief Конструктор валидатора
    #
    # @param board_size Размер игрового поля (по умолчанию 3x3)
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.validation_log = []

    ## @brief Валидация координат хода
    #
    # Проверяет, что координаты находятся в пределах игрового поля
    # и что выбранная клетка не занята.
    #
    # @param row Номер строки (0-based)
    # @param col Номер столбца (0-based)
    # @param board Текущее состояние игрового поля
    #
    # @return Кортеж (is_valid, message) где:
    #         - is_valid (bool): True если ход валиден
    #         - message (str): Сообщение о результате валидации
    def validate_coordinates(self, row, col, board):
        # Проверка границ
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False, f"Coordinates must be between 0 and {self.board_size-1}"

        # Проверка занятости клетки
        if board[row][col] != ' ':
            return False, "Cell is already occupied"

        return True, "Move is valid"

    ## @brief Валидация ручного ввода координат
    #
    # Преобразует текстовый ввод в числовые координаты и проверяет
    # их корректность.
    #
    # @param row_text Текст из поля ввода строки
    # @param col_text Текст из поля ввода столбца
    #
    # @return Кортеж (is_valid, row, col, message) где:
    #         - is_valid (bool): True если ввод валиден
    #         - row (int): Преобразованный номер строки (0-based)
    #         - col (int): Преобразованный номер столбца (0-based)
    #         - message (str): Сообщение о результате валидации

    def validate_manual_input(self, row_text, col_text):
        if not row_text.strip() or not col_text.strip():
            return False, None, None, "Enter both coordinates"

        try:
            row = int(row_text) - 1  # Конвертация в 0-based
            col = int(col_text) - 1
        except ValueError:
            return False, None, None, "Coordinates must be numbers"

        # Проверка границ после конвертации
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False, None, None, f"Coordinates must be between 1 and {self.board_size}"

        return True, row, col, "Coordinates are valid"

    ## @brief Логирование сообщения валидации
    #
    # Добавляет сообщение в историю валидации для последующего
    # анализа и отладки.
    #
    # @param message Сообщение для добавления в лог
    def log_validation(self, message):
        self.validation_log.append(message)

    ## @brief Получение последних записей лога
    #
    # @param count Количество возвращаемых записей (по умолчанию 5)
    #
    # @return Список последних сообщений лога или пустой список
    #         если лог пуст
    def get_recent_logs(self, count=5):
        return self.validation_log[-count:] if self.validation_log else []
