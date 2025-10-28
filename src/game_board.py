## @file game_board.py
## @brief Игровое поле с системой ввода

import tkinter as tk
from tkinter import ttk
from input_handler import InputValidator

## @brief Класс игрового поля с системой ввода
#
# Управляет всем игровым процессом, включая отрисовку интерфейса,
# обработку пользовательского ввода и взаимодействие с валидатором.
class GameBoard:
    
    ## @brief Конструктор класса GameBoard
    #
    # Инициализирует главное окно приложения, игровое состояние
    # и создает графический интерфейс.
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("400x500")  
        self.window.resizable(True, True)  
        self.window.minsize(380, 450)
        
        # Игровое состояние
        self.board_state = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_active = True
        
        # Система ввода и валидации
        self.validator = InputValidator(board_size=3)
        
        self._create_interface()
    
    ## @brief Создание всего графического интерфейса
    #
    # Вызывает методы создания отдельных компонентов интерфейса:
    # заголовка, игрового поля, панели ввода и лог-панели.
    def _create_interface(self):
        self._create_header()
        self._create_game_board()
        self._create_input_panel()
        self._create_log_panel()
    
    ## @brief Создание заголовка и статусной панели
    #
    # Размещает в верхней части окна название игры и индикатор
    # текущего игрока.
    def _create_header(self):
        # Заголовок
        title_label = tk.Label(
            self.window,
            text="Крестики-нолики",
            font=('Arial', 16, 'bold'),
            pady=10
        )
        title_label.pack()
        
        # Статус игры
        self.status_label = tk.Label(
            self.window,
            text=f"Ход игрока: {self.current_player}",
            font=('Arial', 12),
            fg='blue'
        )
        self.status_label.pack()
    
    ## @brief Создание игрового поля с кликабельными клетками
    #
    # Генерирует сетку 3x3 из интерактивных кнопок, каждая из которых
    # привязана к обработчику клика.
    def _create_game_board(self):
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=15)
        
        # Создание клеток поля
        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Button(
                    board_frame,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=4,
                    height=2,
                    bg='white',
                    relief='raised',
                    command=lambda r=row, c=col: self._on_cell_click(r, c)
                )
                cell.grid(row=row, column=col, padx=2, pady=2)
                cell_row.append(cell)
            self.cells.append(cell_row)
    
    ## @brief Создание панели ручного ввода координат
    #
    # Размещает текстовые поля и кнопку для ввода координат
    # с клавиатуры.
    def _create_input_panel(self):
        input_frame = tk.LabelFrame(self.window, text="Ручной ввод координат", font=('Arial', 10))
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # Поля ввода
        controls_frame = tk.Frame(input_frame)
        controls_frame.pack(pady=10)
        
        tk.Label(controls_frame, text="Строка:").grid(row=0, column=0, padx=5)
        self.row_entry = tk.Entry(controls_frame, width=5, justify='center')
        self.row_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(controls_frame, text="Столбец:").grid(row=0, column=2, padx=5)
        self.col_entry = tk.Entry(controls_frame, width=5, justify='center')
        self.col_entry.grid(row=0, column=3, padx=5)
        
        # Кнопка отправки
        submit_btn = tk.Button(
            controls_frame,
            text="Сделать ход",
            command=self._on_manual_input,
            bg='lightgreen'
        )
        submit_btn.grid(row=0, column=4, padx=10)
        
        # Подсказка
        hint_label = tk.Label(
            input_frame,
            text="Введите числа от 1 до 3",
            font=('Arial', 8),
            fg='gray'
        )
        hint_label.pack(pady=5)
    
    ## @brief Создание панели лога валидации
    #
    # Создает текстовое поле для отображения истории действий
    # и сообщений системы валидации.
    def _create_log_panel(self):
        log_frame = tk.LabelFrame(self.window, text="Лог валидации", font=('Arial', 10))
        log_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Текстовое поле лога
        self.log_text = tk.Text(
            log_frame,
            height=6,
            width=40,
            font=('Arial', 9),
            bg='#f8f8f8',
            relief='sunken'
        )
        self.log_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.log_text.insert('end', "Система ввода готова...\n")
        self.log_text.config(state='disabled')
    
    ## @brief Обработчик клика по клетке поля
    #
    # @param row Номер строки (0-based)
    # @param col Номер столбца (0-based)
    def _on_cell_click(self, row, col):
        if not self.game_active:
            self._log_message("Игра не активна")
            return
        
        # Валидация хода
        is_valid, message = self.validator.validate_coordinates(row, col, self.board_state)
        self._log_message(f"Клик ({row+1},{col+1}): {message}")
        
        if is_valid:
            self._execute_move(row, col)
        else:
            self._show_error_animation(row, col)
    
    ## @brief Обработчик ручного ввода координат
    #
    # Читает данные из текстовых полей, валидирует ввод и выполняет ход
    # если координаты корректны и клетка доступна.
    def _on_manual_input(self):
        if not self.game_active:
            self._log_message("Игра не активна")
            return
        
        row_text = self.row_entry.get()
        col_text = self.col_entry.get()
        
        # Валидация ввода
        is_valid, row, col, message = self.validator.validate_manual_input(row_text, col_text)
        self._log_message(f"Ручной ввод: {message}")
        
        if is_valid:
            # Дополнительная валидация хода
            move_valid, move_message = self.validator.validate_coordinates(row, col, self.board_state)
            if move_valid:
                self._execute_move(row, col)
                # Очистка полей ввода
                self.row_entry.delete(0, 'end')
                self.col_entry.delete(0, 'end')
            else:
                self._log_message(f"Ход ({row+1},{col+1}): {move_message}")
                self._show_error_animation(row, col)
    
    ## @brief Выполнение валидного хода
    #
    # Обновляет состояние игры и интерфейс после успешной валидации хода.
    #
    # @param row Номер строки
    # @param col Номер столбца
    def _execute_move(self, row, col):
        # Обновление состояния игры
        self.board_state[row][col] = self.current_player
        
        # Обновление интерфейса
        cell = self.cells[row][col]
        cell.config(
            text=self.current_player,
            state='disabled',
            bg='lightblue' if self.current_player == 'X' else 'lightyellow'
        )
        
        self._log_message(f"✓ Игрок {self.current_player} походил в ({row+1},{col+1})")
        
        # Смена игрока
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Ход игрока: {self.current_player}")
    
    ## @brief Визуальная индикация ошибки
    #
    # Временно подсвечивает клетку красным цветом при невалидном ходе.
    #
    # @param row Номер строки
    # @param col Номер столбца
    def _show_error_animation(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3:
            cell = self.cells[row][col]
            original_color = cell.cget('bg')
            cell.config(bg='red')
            # Возврат исходного цвета через 300ms
            self.window.after(300, lambda: cell.config(bg=original_color))
    
    ## @brief Добавление сообщения в лог
    #
    # Обновляет текстовое поле лога и сохраняет сообщение в системе валидации.
    #
    # @param message Сообщение для добавления в лог
    def _log_message(self, message):
        self.validator.log_validation(message)
        
        # Обновление текстового поля
        self.log_text.config(state='normal')
        self.log_text.insert('end', f"{message}\n")
        
        # Ограничение количества строк
        lines = self.log_text.get(1.0, 'end').split('\n')
        if len(lines) > 10:
            self.log_text.delete(1.0, 2.0)
        
        self.log_text.see('end')
        self.log_text.config(state='disabled')
    
    ## @brief Запуск главного цикла приложения
    #
    # Запускает обработку событий Tkinter и отображение интерфейса.
    def run(self):
        self.window.mainloop()