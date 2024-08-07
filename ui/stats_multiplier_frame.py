import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, Scrollbar, Toplevel

from functions.stats_transformer import transform_stats_data_to_config

# Définitions des stats
STATS_LABELS = [
    "Santé", "Endurance", "Torpeur",
    "Oxygène", "Nourriture", "Eau", "Température",
    "Poids", "Mêlée", "Vitesse", "Résistance climatique",
    "Fabrication"
]

# Valeurs par défaut
default_player_stats = [10] * 12
default_dino_tamed_stats = [10] * 12
default_dino_wild_stats = [2] * 12

def open_stats_multiplier_window():
    # Créer une nouvelle fenêtre (Toplevel) pour la configuration des multiplicateurs de stats
    stats_window = Toplevel()
    stats_window.title("Configuration des Multiplicateurs de Stats")
    stats_window.geometry("800x600")

    # Créer un canvas pour permettre le défilement
    canvas = Canvas(stats_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Ajouter une barre de défilement verticale
    scrollbar = Scrollbar(stats_window, orient="vertical", command=canvas.yview)
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
    stats_window.bind_all("<MouseWheel>", on_mouse_wheel)

    # Créer les en-têtes du tableau
    headers = ["Statistique", "Joueur", "Dino Apprivoisé", "Dino Sauvage"]
    for col, header in enumerate(headers):
        Label(scrollable_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=5, pady=5)

    # Listes pour stocker les références des widgets d'entrée
    player_entries = []
    dino_tamed_entries = []
    dino_wild_entries = []

    # Remplir le tableau avec les données par défaut
    for i, stat_label in enumerate(STATS_LABELS):
        row = i + 1
        Label(scrollable_frame, text=stat_label).grid(row=row, column=0, padx=5, pady=5, sticky="w")

        player_entry = Entry(scrollable_frame)
        player_entry.insert(0, default_player_stats[i])
        player_entry.grid(row=row, column=1, padx=5, pady=5)
        player_entries.append(player_entry)

        dino_tamed_entry = Entry(scrollable_frame)
        dino_tamed_entry.insert(0, default_dino_tamed_stats[i])
        dino_tamed_entry.grid(row=row, column=2, padx=5, pady=5)
        dino_tamed_entries.append(dino_tamed_entry)

        dino_wild_entry = Entry(scrollable_frame)
        dino_wild_entry.insert(0, default_dino_wild_stats[i])
        dino_wild_entry.grid(row=row, column=3, padx=5, pady=5)
        dino_wild_entries.append(dino_wild_entry)

    # Fonction pour sauvegarder les données et fermer la fenêtre
    def save_and_close():
        player_stats = [float(entry.get()) for entry in player_entries]
        dino_tamed_stats = [float(entry.get()) for entry in dino_tamed_entries]
        dino_wild_stats = [float(entry.get()) for entry in dino_wild_entries]

        config_text = transform_stats_data_to_config(player_stats, dino_tamed_stats, dino_wild_stats)
        
        # Afficher les valeurs pour vérification
        print(config_text)

        stats_window.destroy()

    # Ajouter un bouton pour fermer et sauvegarder en bas du tableau avec des marges
    close_button = Button(scrollable_frame, text="Sauvegarder et Fermer", command=save_and_close)
    close_button.grid(row=len(STATS_LABELS) + 1, column=0, columnspan=4, pady=20)

    # Sauvegarder les données à la fermeture de la fenêtre via la croix
    stats_window.protocol("WM_DELETE_WINDOW", save_and_close)

    # Mettre à jour la taille du canvas pour correspondre à la taille du contenu
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
