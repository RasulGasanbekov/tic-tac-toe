"""
@file game_board.py
@brief Класс для создания графического игрового поля
"""

import tkinter as tk

class GameBoard:
    """
    @brief Класс игрового поля (только визуальная часть)
    """
    
    def __init__(self):
        """
        @brief Конструктор - создает пустое поле 3x3
        """
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("300x300")
        self.window.resizable(False, False)
        
        # Игровое поле (только визуальное, без логики)
        self.board_state = [
            [' ', ' ', ' '],
            [' ', ' ', ' '], 
            [' ', ' ', ' ']
        ]
        
        self._create_visual_interface()
    
    def _create_visual_interface(self):
        """
        @brief Создание визуального интерфейса поля
        @return: None
        """
        # Заголовок
        title_label = tk.Label(
            self.window,
            text="Крестики-нолики",
            font=('Arial', 16, 'bold'),
            pady=20
        )
        title_label.pack()
        
        # Игровое поле
        self._create_board_grid()
        
        # Статус
        status_label = tk.Label(
            self.window,
            text="Графическое поле создано",
            font=('Arial', 10),
            pady=20
        )
        status_label.pack()
    
    def _create_board_grid(self):
        """
        @brief Создание сетки игрового поля
        @return: None
        """
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=10)
        
        # Создание клеток (только визуал, без функциональности)
        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Label(
                    board_frame,
                    text=" ",
                    font=('Arial', 20),
                    width=3,
                    height=1,
                    relief='solid',
                    borderwidth=2,
                    bg='white'
                )
                cell.grid(row=row, column=col, padx=2, pady=2)
                cell_row.append(cell)
            self.cells.append(cell_row)
    
    def run(self):
        """
        @brief Запуск графического приложения
        @return: None
        """
        self.window.mainloop()