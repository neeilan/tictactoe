import tkinter as tk
from functools import partial

from ttt import MinimaxTTT

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.p1_symbol = 'X'
        self.p2_symbol = 'O'
        self.buttons = []
        self.ttt = MinimaxTTT()
        self._create_buttons()   
        
    def _on_click(self, i):
        if self.ttt.get_cell(i) is None and self.ttt.get_winner() is None:
            self.ttt.user_move(i)
            self._update_view()
            self.check_winner()
            
    def check_winner(self):
        winner = self.ttt.get_winner()
        if winner == -1:
            print("You win")
        elif winner == 1:
            print("You lose")
        elif winner == 0:
            print("Tie!")
        
    def _create_buttons(self):
        for i in range(9):
            btn = tk.Button(self, height = 8, width = 16, command = partial(self._on_click, i))
            btn.grid(row = (i // 3) + 1, column = (i % 3) + 1)
            self.buttons.append(btn)
        
    def _update_view(self):
        for i in range(9):
            symbol = ''
            user = self.ttt.get_cell(i)
            if user == 1:
                symbol = self.p1_symbol
            elif user == -1:
                symbol = self.p2_symbol
            self.buttons[i].config(text= symbol)


if __name__ == '__main__':
    app = Application() 
    app.master.title('Unbeatable TicTacToe')
    app.mainloop()
