import tkinter as tk
import random as rnd

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.board = [[0] * 4 for _ in range(4)]
        self.matrix=[[0] * 4 for _ in range(4)]
        self.matriz_guide=[[0] * 4 for _ in range(4)]
        self.setup_ui()

    def setup_ui(self):
        for row in range(4):
            for column in range(4): 
                cell = tk.Label(
                    root,
                    text="",
                    borderwidth=1,
                    relief="solid",
                    width=10,
                    height=5,
                    bg="#003322",
                )
                cell.grid(row=row, column=column, padx=0, pady=0)
                self.matrix[row][column] = cell
            
        
        i=rnd.randint(0,3)
        j=rnd.randint(0,3)
        self.matrix[i][j].config(bg="#120034")
        while 1:
            a=rnd.randint(0,3)
            b=rnd.randint(0,3)
            self.matrix[a][b].config(bg="#120034")
            if a!=i or b!=j:
                break
            
         
            
            
            
            
            
            
            
            
                
        

if __name__ == "__main__":
    root = tk.Tk()
    game = App(root)
    root.mainloop()
