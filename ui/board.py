import tkinter as tk

class BoardUI:
    def __init__(self, root, n, cell_size=60):
        self.n = n
        self.cell_size = cell_size
        self.canvas = tk.Canvas(
            root,
            width=n * cell_size,
            height=n * cell_size
        )
        self.canvas.pack()

    def draw(self, board):
        self.canvas.delete("all")

        for r in range(self.n):
            for c in range(self.n):
                color = "#EEE" if (r + c) % 2 == 0 else "#666"
                self.canvas.create_rectangle(
                    c * self.cell_size,
                    r * self.cell_size,
                    (c + 1) * self.cell_size,
                    (r + 1) * self.cell_size,
                    fill=color
                )

        for r, c in enumerate(board):
            if c != -1:
                x = c * self.cell_size + self.cell_size // 2
                y = r * self.cell_size + self.cell_size // 2
                self.canvas.create_text(
                    x, y, text="♛",
                    font=("Arial", self.cell_size // 1),
                    fill="red"
                )
