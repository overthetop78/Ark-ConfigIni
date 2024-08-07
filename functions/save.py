# File: functions/save.py

from tkinter import filedialog, messagebox

def save_to_file(data):
    save_path = filedialog.asksaveasfilename(defaultextension=".ini", filetypes=[("INI files", "*.ini")])
    if save_path:
        with open(save_path, 'w') as f:
            f.write(data)
        messagebox.showinfo("Succès", "Fichier généré avec succès !")
    else:
        messagebox.showwarning("Annulé", "Enregistrement annulé.")
