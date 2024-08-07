# File: ui/engram_points_frame.py
import tkinter as tk


class EngramPointsFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.init_ui()

    def init_ui(self):
        # Nombre de points minimum
        tk.Label(self, text="Nombre de points minimum :").pack()
        self.entry_start_points = tk.Entry(self)
        self.entry_start_points.pack()

        # Nombre de niveaux pour débloquer tous les engrammes
        tk.Label(self, text="Niveaux pour débloquer tous les engrammes :").pack()
        self.entry_levels_to_unlock_all = tk.Entry(self)
        self.entry_levels_to_unlock_all.pack()

        # Type d'incrémentation des points
        tk.Label(self, text="Type d'incrémentation des points :").pack()
        self.increment_type = tk.StringVar(value="linear")
        tk.Radiobutton(self, text="Linéaire", variable=self.increment_type, value="linear", command=self.toggle_options).pack(anchor="w")
        tk.Radiobutton(self, text="Incrémental", variable=self.increment_type, value="incremental", command=self.toggle_options).pack(anchor="w")
        tk.Radiobutton(self, text="Exponentiel", variable=self.increment_type, value="exponential", command=self.toggle_options).pack(anchor="w")

        # Nombre de points maximum (visible si non-linéaire)
        self.label_max_points = tk.Label(self, text="Nombre de points maximum :")
        self.entry_max_points = tk.Entry(self)

        # Nombre de niveaux avant d'augmenter (visible si non-linéaire)
        self.label_levels_increment = tk.Label(self, text="Niveaux avant augmentation :")
        self.entry_levels_increment = tk.Entry(self)

    def toggle_options(self):
        """Afficher ou masquer les options en fonction du type d'incrémentation."""
        increment_type = self.increment_type.get()
        if increment_type == "linear":
            self.label_max_points.pack_forget()
            self.entry_max_points.pack_forget()
            self.label_levels_increment.pack_forget()
            self.entry_levels_increment.pack_forget()
        else:
            self.label_max_points.pack(pady=(10, 0))
            self.entry_max_points.pack(pady=(0, 10))
            self.label_levels_increment.pack(pady=(10, 0))
            self.entry_levels_increment.pack(pady=(0, 10))
