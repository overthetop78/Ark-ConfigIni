def transform_stats_data_to_config(player_stats, dino_tamed_stats, dino_wild_stats):
    config_lines = []

    # Ajouter les lignes pour les joueurs
    for i, value in enumerate(player_stats):
        config_lines.append(f"PerLevelStatsMultiplier_Player[{i}]={value}")

    # Ajouter les lignes pour les dinos apprivoisés
    for i, value in enumerate(dino_tamed_stats):
        config_lines.append(f"PerLevelStatsMultiplier_DinoTamed[{i}]={value}")

    # Ajouter les lignes pour les dinos sauvages
    for i, value in enumerate(dino_wild_stats):
        config_lines.append(f"PerLevelStatsMultiplier_DinoWild[{i}]={value}")

    return "\n".join(config_lines)
