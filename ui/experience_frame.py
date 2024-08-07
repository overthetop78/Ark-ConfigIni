# File: ui/experience_frame.py
import tkinter as tk


class ExperienceFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.init_ui()

    def init_ui(self):
        tk.Label(self, text="Nombre de niveaux :").pack()
        self.entry_levels = tk.Entry(self)
        self.entry_levels.pack()

        tk.Label(self, text="XP de base (recommandé: 10) :").pack()
        self.entry_base_xp = tk.Entry(self)
        self.entry_base_xp.pack()

        tk.Label(self, text="Multiplicateur de progression (recommandé: 1.8) :").pack()
        self.entry_multiplier = tk.Entry(self)
        self.entry_multiplier.pack()

        self.var_experience_type = tk.StringVar(value="joueurs_dinos")
        tk.Radiobutton(self, text="Joueurs et Dinos", variable=self.var_experience_type, value="joueurs_dinos").pack(anchor="w")
        tk.Radiobutton(self, text="Joueurs seulement", variable=self.var_experience_type, value="joueurs").pack(anchor="w")
