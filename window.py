import tkinter as tk

from generate_experience import generate_experience_levels


def launch():
    root = tk.Tk()
    root.title("Générateur de Niveaux d'Expérience ARK")
    root.geometry("400x400")  # Agrandir la fenêtre

    # Création des champs de saisie
    label_levels = tk.Label(root, text="Nombre de niveaux :")
    label_levels.pack()
    entry_levels = tk.Entry(root)
    entry_levels.pack()

    label_base_xp = tk.Label(root, text="XP de base (recommandé: 10) :")
    label_base_xp.pack()
    entry_base_xp = tk.Entry(root)
    entry_base_xp.pack()

    label_multiplier = tk.Label(root, text="Multiplicateur de progression (recommandé: 1.8) :")
    label_multiplier.pack()
    entry_multiplier = tk.Entry(root)
    entry_multiplier.pack()

    # Options pour choisir entre joueurs, dinosaures sauvages et apprivoisés
    var_players = tk.BooleanVar()
    check_players = tk.Checkbutton(root, text="Joueurs", variable=var_players)
    check_players.pack()

    var_wild_dinos = tk.BooleanVar()
    check_wild_dinos = tk.Checkbutton(root, text="Dinosaures sauvages", variable=var_wild_dinos)
    check_wild_dinos.pack()

    var_tamed_dinos = tk.BooleanVar()
    check_tamed_dinos = tk.Checkbutton(root, text="Dinosaures apprivoisés", variable=var_tamed_dinos)
    check_tamed_dinos.pack()

    def generate_file():
        num_levels = int(entry_levels.get())
        base_xp = float(entry_base_xp.get())
        multiplier = float(entry_multiplier.get())
        
        player_enabled = var_players.get()
        wild_dino_enabled = var_wild_dinos.get()
        tamed_dino_enabled = var_tamed_dinos.get()
        
        generate_experience_levels(num_levels, base_xp, multiplier, player_enabled, wild_dino_enabled, tamed_dino_enabled)

    # Bouton pour générer le fichier
    button_generate = tk.Button(root, text="Générer le fichier", command=generate_file)
    button_generate.pack()

    root.mainloop()
