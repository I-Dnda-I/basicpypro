import tkinter as tk
import random as rnd


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.matrix = [[0] * 4 for _ in range(4)]
        self.matrix_guide = [[0] * 4 for _ in range(4)]
        self.setup_start()
        self.random_start()

        self.root.bind("<Right>", self.event_r_arrow)
        self.root.bind("<Left>", self.event_l_arrow)
        self.root.bind("<Up>", self.event_u_arrow)
        self.root.bind("<Down>", self.event_d_arrow)

    def setup_start(self):
        for row in range(4):
            for column in range(4):
                cell = tk.Label(
                    root,
                    text="",
                    font=("Helvetica", 25),
                    borderwidth=1,
                    relief="solid",
                    width=10,
                    height=5,
                    bg="#ffffff",
                )
                cell.grid(row=row, column=column, padx=0, pady=0)
                self.matrix[row][column] = cell

    def random_start(self):
        i = rnd.randint(0, 3)
        j = rnd.randint(0, 3)
        self.matrix_guide[i][j] = 2
        self.matrix[i][j].config(bg="#00dddd", text=f"{self.matrix_guide[i][j]}")
        while 1:
            a = rnd.randint(0, 3)
            b = rnd.randint(0, 3)
            if a != i or b != j:
                self.matrix_guide[a][b] = 2
                self.matrix[a][b].config(
                    bg="#00dddd", text=f"{self.matrix_guide[a][b]}"
                )
                break

    def random_mvmnt(self):
        while 1:
            i = rnd.randint(0, 3)
            j = rnd.randint(0, 3)
            if self.matrix_guide[i][j] == 0:
                self.matrix_guide[i][j] = rnd.choices([2, 4], weights=[0.75, 0.25])[0]
                self.matrix[i][j].config(
                    bg="#00dddd", text=f"{self.matrix_guide[i][j]}"
                )
                break

    def fusion_cells_to_r(self):
        self.mov_cells_to_r()
        for i in range(3, -1, -1):
            for j in range(3, -1, -1):
                if j + 1 < 4 and self.matrix_guide[i][j + 1] == self.matrix_guide[i][j]:
                    self.matrix_guide[i][j + 1] = self.matrix_guide[i][j + 1] * 2
                    self.matrix_guide[i][j] = 0
        self.mov_cells_to_r()

    def fusion_cells_to_l(self):
        self.mov_cells_to_l()
        for i in range(4):
            for j in range(4):
                if j + 1 < 4 and self.matrix_guide[i][j + 1] == self.matrix_guide[i][j]:
                    self.matrix_guide[i][j] = self.matrix_guide[i][j] * 2
                    self.matrix_guide[i][j + 1] = 0
        self.mov_cells_to_l()

    def fusion_cells_to_u(self):
        self.mov_cells_to_u()
        for i in range(4):
            for j in range(3, -1, -1):
                if i + 1 < 4 and self.matrix_guide[i][j] == self.matrix_guide[i+1][j]:
                    self.matrix_guide[i][j] = self.matrix_guide[i][j] * 2
                    self.matrix_guide[i+1][j] = 0
        self.mov_cells_to_u()

    def fusion_cells_to_d(self):
        self.mov_cells_to_d()
        for i in range(3, -1, -1):
            for j in range(3, -1, -1):
                if i + 1 < 4 and self.matrix_guide[i+1][j] == self.matrix_guide[i][j]:
                    self.matrix_guide[i+1][j] = self.matrix_guide[i+1][j] * 2
                    self.matrix_guide[i][j] = 0
        print(self.matrix_guide)
        self.mov_cells_to_d()

    def mov_cells_to_r(self):
        for i in range(3, -1, -1):
            for j in range(3, -1, -1):
                for k in range(j + 1, 4, 1):
                    if not (self.matrix_guide[i][k] == 0):
                        if k - 1 != j:
                            self.matrix_guide[i][k - 1] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break

                    if k == 3:
                        self.matrix_guide[i][k] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break

    def mov_cells_to_l(self):
        for i in range(4):
            for j in range(4):
                for k in range(j - 1, -1, -1):
                    if not (self.matrix_guide[i][k] == 0):
                        if k + 1 != j:
                            self.matrix_guide[i][k + 1] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break

                    if k == 0:
                        self.matrix_guide[i][k] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break
        print(f" moves : {self.matrix_guide}")
        
    def mov_cells_to_u(self):
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(i-1, -1, -1):
                    if not (self.matrix_guide[k][j] == 0):
                        if k + 1 != i:
                            self.matrix_guide[k+1][j] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break

                    if k == 0:
                        self.matrix_guide[k][j] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break
    
    def mov_cells_to_d(self):
        for i in range(3, -1, -1):
            for j in range(3, -1, -1):
                for k in range(i + 1, 4, 1):
                    if not (self.matrix_guide[k][j] == 0):
                        if k - 1 != i:
                            self.matrix_guide[k-1][j] = self.matrix_guide[i][j]
                            self.matrix_guide[i][j] = 0
                        break

                    if k == 3:
                        self.matrix_guide[k][j] = self.matrix_guide[i][j]
                        self.matrix_guide[i][j] = 0
                        break
                    
    def update_game(self):
        for i in range(4):
            for j in range(4):
                if self.matrix_guide[i][j] > 0:
                    self.matrix[i][j].config(
                        bg="#00dddd", text=f"{self.matrix_guide[i][j]}"
                    )
                else:
                    self.matrix[i][j].config(bg="#ffffff", text="")

    def restart_state(self):
        for i in range(4):
            for j in range(4):
                self.matrix[i][j].config(bg="#ffffff", text="")
                self.matrix_guide[i][j] = 0
        self.random_start()

    def verify_full(self):
        for i in range(4):
            for j in range(4):
                if self.matrix_guide[i][j] == 0:
                    return False
        return True

    def event_r_arrow(self, event):
        self.fusion_cells_to_r()  # to determine if there is no more movements available is a must to press right arrow
        if self.verify_full():
            self.restart_state()
        else:
            self.random_mvmnt()
            self.update_game()

    def event_l_arrow(self, event):
        self.fusion_cells_to_l()  
        if self.verify_full():
            self.restart_state()
        else:
            self.random_mvmnt()
            self.update_game()
    def event_u_arrow(self, event):
        self.fusion_cells_to_u()  
        if self.verify_full():
            self.restart_state()
        else:
            self.random_mvmnt()
            self.update_game()
    def event_d_arrow(self, event):
        self.fusion_cells_to_d()  
        if self.verify_full():
            self.restart_state()
        else:
            self.random_mvmnt()
            self.update_game()      
if __name__ == "__main__":
    root = tk.Tk()
    game = App(root)
    root.mainloop()
