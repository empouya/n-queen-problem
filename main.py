import tkinter as tk
from state import AppState
from algorithms.backtracking import BacktrackingAlgorithm
from ui.board import BoardUI
from ui.controls import ControlsUI

N = 8

root = tk.Tk()
root.title("N-Queens Visualizer")

app = tk.Frame(root, padx=30, pady=30)
app.pack(fill=tk.BOTH, expand=True)

state = AppState()
board_ui = BoardUI(app, N)

def start():
    if not state.running:
        algo = BacktrackingAlgorithm(N)
        state.algorithm = algo
        state.iterator = algo.run()
        state.running = True
        step()

def pause():
    state.running = False

def step():
    if not state.running:
        return
    try:
        board = next(state.iterator)
        board_ui.draw(board)
        controls.update_steps(state.algorithm.steps)
        root.after(state.speed, step)
    except StopIteration:
        state.running = False

controls = ControlsUI(app, state, start, pause)

root.mainloop()
