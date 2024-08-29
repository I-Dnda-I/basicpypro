import tkinter as tk
import random as rnd

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.matrix = [[0] * 4 for _ in range(4)]
        self.matrix_guide=[[0] * 4 for _ in range(4)]
        self.setup_start()
        self.random_start()

        self.root.bind("<Right>", self.event_r_arrow)
        
        
        
    def setup_start(self):
        for row in range(4):
            for column in range(4): 
                cell = tk.Label(
                    root,
                    text="",
                    borderwidth=1,
                    relief="solid",
                    width=10,
                    height=5,
                    bg="#ffffff",
                )
                cell.grid(row=row, column=column, padx=0, pady=0)
                self.matrix[row][column] = cell
            
    def random_start(self):
        
        i=rnd.randint(0,3)
        j=rnd.randint(0,3)
        self.matrix_guide[i][j]=2
        self.matrix[i][j].config(bg="#00dddd", text=f"{self.matrix_guide[i][j]}")
        while 1:
            a=rnd.randint(0,3)
            b=rnd.randint(0,3)
            if a!=i or b!=j:
                self.matrix_guide[a][b]=2
                self.matrix[a][b].config(bg="#00dddd", text=f"{self.matrix_guide[a][b]}")
                break
        
    def random_mvmnt(self):
        while 1:
            i=rnd.randint(0,3)
            j=rnd.randint(0,3)
            if self.matrix_guide[i][j]==0:
                print(self.matrix_guide)
                self.matrix_guide[i][j]=rnd.choices([2,4],weights=[0.75,0.25])[0]
                self.matrix[i][j].config(bg="#00dddd", text=f"{self.matrix_guide[i][j]}")
                break
                
    def mov_cells_to_r(self):
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                for k in range(j+1,4,1):
                    if not (self.matrix_guide[i][k]==0):
                        if k-1!= j:
                            self.matrix_guide[i][k-1] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break      
                    
                    if (k==3):
                        self.matrix_guide[i][k] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break
                        
                if j+1<4 and self.matrix_guide[i][j+1]==self.matrix_guide[i][j]:
                    self.matrix_guide[i][j+1]=self.matrix_guide[i][j+1]*2
                    self.matrix_guide[i][j]=0
                
                for k in range(j+1,4,1):
                    if not (self.matrix_guide[i][k]==0):
                        if k-1!= j:
                            self.matrix_guide[i][k-1] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break      
                    
                    if (k==3):
                        self.matrix_guide[i][k] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break
                        
                
    def update_game(self):
        for i in range(4):
            for j in range(4):
                if self.matrix_guide[i][j]>0:
                    self.matrix[i][j].config(bg="#00dddd", text=f"{self.matrix_guide[i][j]}")
                else:
                    self.matrix[i][j].config(bg="#ffffff", text="")
    
    def restart_state(self):
        for i in range(4):
            for j in range(4):
                self.matrix[i][j].config(bg="#ffffff",text="")
                self.matrix_guide[i][j]=0
        self.random_start()
    
    def verify_full():
        pass
    
    def event_r_arrow(self,event):
        self.mov_cells_to_r()
        if not self.verify_full():
            self.restart_state()
        else:
            self.random_mvmnt()
            self.update_game()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = App(root)
    root.mainloop()
