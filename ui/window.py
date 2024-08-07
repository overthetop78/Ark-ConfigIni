# File: ui/window.py
import tkinter as tk

from ui.engram_config_frame import open_engram_config_window
from ui.engram_points_frame import EngramPointsFrame
from ui.experience_frame import ExperienceFrame
from ui.log_frame import LogFrame
from ui.stats_multiplier_frame import \
    open_stats_multiplier_window  # Importer la nouvelle fonction


def launch():
    root = tk.Tk()
    root.title("Création de fichier Game.ini pour Ark")
    root.geometry("1200x1024")  # Agrandir la fenêtre

    # Ajouter les frames avec bordures et titres
    experience_frame = tk.LabelFrame(root, text="Paramètres d'Expérience", borderwidth=2, relief="groove")
    experience_frame.pack(side="top", fill="none", padx=10, pady=5, anchor="w")
    ExperienceFrame(experience_frame).pack(fill="both", expand=True)

    engram_points_frame = tk.LabelFrame(root, text="Configuration des Points Engrammes", borderwidth=2, relief="groove")
    engram_points_frame.pack(side="top", fill="none", padx=10, pady=5, anchor="w")
    EngramPointsFrame(engram_points_frame).pack(fill="both", expand=True)

    points_frame = tk.LabelFrame(root, text="Répartition des Points", borderwidth=2, relief="groove")
    points_frame.pack(side="top", fill="none", padx=10, pady=5, anchor="w")

    open_engram_button = tk.Button(points_frame, text="Configurer les Engrammes", command=open_engram_config_window)
    open_engram_button.pack(pady=10)  # Ajouter une marge en bas

    # Ajouter un cadre pour la configuration des multiplicateurs de stats
    stats_multiplier_frame = tk.LabelFrame(root, text="Configuration des Multiplicateurs de Stats", borderwidth=2, relief="groove")
    stats_multiplier_frame.pack(side="top", fill="none", padx=10, pady=5, anchor="w")

    open_stats_button = tk.Button(stats_multiplier_frame, text="Configurer les Multiplicateurs de Stats", command=open_stats_multiplier_window)
    open_stats_button.pack(pady=10)  # Ajouter une marge en bas

    log_frame = LogFrame(root)
    log_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    # Exemple d'ajout de log
    log_frame.log("L'application a démarré.")
    log_frame.log("Paramètres d'expérience initialisés.")

    # Boucle principale de l'interface
    root.mainloop()
