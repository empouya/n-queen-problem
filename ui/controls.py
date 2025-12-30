import tkinter as tk
from tkinter import ttk

class ControlsUI:
    def __init__(self, parent, state, start_callback, pause_callback):
        container = tk.Frame(parent)
        container.pack(fill=tk.X, pady=(15, 0))

        # Algorithm selector button
        tk.Label(container, text="Algorithm:", font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 6))

        self.algorithm_var = tk.StringVar(value="Backtracking")
        algo_menu = ttk.Combobox(
            container,
            textvariable=self.algorithm_var,
            state="readonly",
            width=15,
            values=["Backtracking"]
        )
        algo_menu.pack(side=tk.LEFT, padx=(0, 12))
        algo_menu.bind("<<ComboboxSelected>>", lambda e: algo_change_cb(self.algorithm_var.get()))

        # Control buttons
        tk.Button(
            container,
            text="▶ Start",
            width=8,
            relief=tk.FLAT,
            command=start_callback,
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            container,
            text="⏸ Pause",
            width=8,
            relief=tk.FLAT,
            command=pause_callback
        ).pack(side=tk.LEFT, padx=(0, 12))

        # Speed
        tk.Label(container, text="Speed", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.speed = tk.Scale(
            container,
            from_=50,
            to=1000,
            orient=tk.HORIZONTAL,
            showvalue=True,
            length=160,
            command=lambda v: setattr(state, "speed", int(v))
        )

        self.speed.set(state.speed)
        self.speed.pack(side=tk.LEFT, padx=(6, 12))

        # steps
        self.steps_label = tk.Label(container, text="Steps: 0",  font=("Segoe UI", 10, "bold"))
        self.steps_label.pack(side=tk.RIGHT)

    def update_steps(self, steps):
        self.steps_label.config(text=f"Steps: {steps}")
