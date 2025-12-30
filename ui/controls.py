import tkinter as tk

class ControlsUI:
    def __init__(self, root, state, start_callback, pause_callback):
        frame = tk.Frame(root)
        frame.pack(fill=tk.X)

        tk.Button(frame, text="▶ Start", command=start_callback).pack(side=tk.LEFT)
        tk.Button(frame, text="⏸ Pause", command=pause_callback).pack(side=tk.LEFT)

        tk.Label(frame, text="Speed").pack(side=tk.LEFT)
        self.speed = tk.Scale(frame, from_=50, to=1000,
                              orient=tk.HORIZONTAL,
                              command=lambda v: setattr(state, "speed", int(v)))
        self.speed.set(state.speed)
        self.speed.pack(side=tk.LEFT)

        self.steps_label = tk.Label(frame, text="Steps: 0")
        self.steps_label.pack(side=tk.RIGHT)

    def update_steps(self, steps):
        self.steps_label.config(text=f"Steps: {steps}")
