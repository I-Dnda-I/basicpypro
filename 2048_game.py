import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.board = [[0] * 4 for _ in range(4)]
        self.labels = [[None] * 4 for _ in range(4)]
        self.setup_ui()

    def setup_ui(self):
        for row in range(4):
            for column in range(4): 
                cell = tk.Label(
                    root,
                    text=f"Cell {row*4 + column + 1}",
                    borderwidth=1,
                    relief="solid",
                    width=10,
                    height=5,
                )
                cell.grid(row=row, column=column, padx=0, pady=0)


if __name__ == "__main__":
    root = tk.Tk()
    game = App(root)
    root.mainloop()
