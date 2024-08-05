from save import save_to_file


def generate_experience_levels(num_levels, base_xp, multiplier, player_enabled, wild_dino_enabled, tamed_dino_enabled):
    experience_points_players = [0]
    experience_points_dinos = [0]
    experience_points_tamed_dinos = [0]

    for level in range(1, num_levels + 1):
        xp_player = base_xp * (level ** multiplier)
        xp_dino = (base_xp / 1.5) * (level ** multiplier)
        xp_tamed_dino = (base_xp / 2) * (level ** multiplier)
        
        experience_points_players.append(int(xp_player))
        experience_points_dinos.append(int(xp_dino))
        experience_points_tamed_dinos.append(int(xp_tamed_dino))

    result = "[/script/shootergame.shootergamemode]\n"
    if player_enabled:
        result += generate_section("LevelExperienceRampOverrides", experience_points_players)
    if wild_dino_enabled:
        result += generate_section("LevelExperienceRampOverrides", experience_points_dinos)
    if tamed_dino_enabled:
        result += generate_section("LevelExperienceRampOverrides", experience_points_tamed_dinos)

    save_to_file(result)

def generate_section(section_name, experience_points):
    section = f"{section_name}=(ExperiencePointsForLevel[0]={experience_points[0]}"
    for i in range(1, len(experience_points)):
        section += f",ExperiencePointsForLevel[{i}]={experience_points[i]}"
    section += ")\n"
    return section
