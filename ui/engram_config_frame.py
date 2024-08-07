import tkinter as tk
from tkinter import Button, Canvas, Frame, Scrollbar, Toplevel

from constants.engram_const import ENGRAMS

# Variable pour stocker les données des engrammes
engram_data = ENGRAMS.copy()

def open_engram_config_window():
    global engram_data

    # Créer une nouvelle fenêtre (Toplevel) pour la configuration des engrammes
    config_window = Toplevel()
    config_window.title("Configuration des Engrammes")
    config_window.geometry("800x600")

    # Créer un canvas pour permettre le défilement
    canvas = Canvas(config_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Ajouter une barre de défilement verticale
    scrollbar = Scrollbar(config_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    # Frame qui contiendra tous les widgets
    scrollable_frame = Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Attacher le canvas à la scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Fonction pour faire défiler avec la molette de la souris
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Lier l'événement de la molette de la souris au canvas
    config_window.bind_all("<MouseWheel>", on_mouse_wheel)

    # Créer les en-têtes du tableau
    headers = ["Nom", "Level Requis", "Points Requis", "Cacher", "Pré-requis"]
    for col, header in enumerate(headers):
        tk.Label(scrollable_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=5, pady=5)

    # Listes pour stocker les références des widgets d'entrée
    level_entries = []
    points_entries = []
    hidden_vars = []
    prereq_vars = []

    # Remplir le tableau avec les données des engrammes
    for i, engram in enumerate(engram_data):
        row = i + 1
        tk.Label(scrollable_frame, text=engram["display_name"]).grid(row=row, column=0, padx=5, pady=5, sticky="w")
        
        level_entry = tk.Entry(scrollable_frame)
        level_entry.insert(0, engram["level"])
        level_entry.grid(row=row, column=1, padx=5, pady=5)
        level_entries.append(level_entry)
        
        points_entry = tk.Entry(scrollable_frame)
        points_entry.insert(0, engram["points"])
        points_entry.grid(row=row, column=2, padx=5, pady=5)
        points_entries.append(points_entry)
        
        hidden_var = tk.BooleanVar(value=engram["hidden"])
        tk.Checkbutton(scrollable_frame, variable=hidden_var).grid(row=row, column=3, padx=5, pady=5)
        hidden_vars.append(hidden_var)

        prereq_var = tk.BooleanVar(value=engram["requires_prereq"])
        tk.Checkbutton(scrollable_frame, variable=prereq_var).grid(row=row, column=4, padx=5, pady=5)
        prereq_vars.append(prereq_var)

    # Fonction pour sauvegarder les données et fermer la fenêtre
    def save_and_close():
        # Récupérer les données des entrées
        for idx, engram in enumerate(engram_data):
            engram["level"] = int(level_entries[idx].get())
            engram["points"] = int(points_entries[idx].get())
            engram["hidden"] = hidden_vars[idx].get()
            engram["requires_prereq"] = prereq_vars[idx].get()
        config_window.destroy()
        # Appeler la fonction pour transformer les données et les afficher
        from functions.transform_engram_data import \
            transform_engram_data_to_override_format
        override_entries = transform_engram_data_to_override_format(engram_data)
        for entry in override_entries:
            print(entry)

    # Ajouter un bouton pour fermer et sauvegarder en bas du tableau avec des marges
    close_button = Button(scrollable_frame, text="Sauvegarder et Fermer", command=save_and_close)
    close_button.grid(row=len(engram_data) + 1, column=0, columnspan=5, pady=20)

    # Sauvegarder les données à la fermeture de la fenêtre via la croix
    config_window.protocol("WM_DELETE_WINDOW", save_and_close)

    # Mettre à jour la taille du canvas pour correspondre à la taille du contenu
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
