# File: ui/log_frame.py
import tkinter as tk
from tkinter import scrolledtext


class LogFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.label = tk.Label(self, text="Log:", fg="lime", bg="black")
        self.label.pack(anchor="w")

        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10, bg="black", fg="lime")
        self.text_area.pack(fill="both", expand=True)
        self.text_area.config(state=tk.DISABLED)

    def log(self, message):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)
