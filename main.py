# File: main.py
# Description: Fichier principal du programme 
# main.py est le fichier principal du programme. Il importe le module window.py et lance la fenêtre principale de l'application.

import logging

import ui.window as window

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Lancement de l'application")
        window.launch()
    except Exception as e:
        logging.error(f"Erreur lors de l'exécution de l'application : {e}")

if __name__ == "__main__":
    main()
