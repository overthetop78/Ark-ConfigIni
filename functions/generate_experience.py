# File: functions/generate_experience.py

def generate_experience_levels(num_levels, base_xp, multiplier, experience_type):
    experience_points_players = [0]
    experience_points_tamed_dinos = [0]

    for level in range(1, num_levels + 1):
        xp_player = base_xp * (level ** multiplier)
        xp_tamed_dino = (base_xp / 2) * (level ** multiplier)

        experience_points_players.append(int(xp_player))
        experience_points_tamed_dinos.append(int(xp_tamed_dino))

    result = "[/script/shootergame.shootergamemode]\n"
    if experience_type == "joueurs_dinos":
        result += generate_section("LevelExperienceRampOverrides", experience_points_players)
        result += generate_section("LevelExperienceRampOverrides", experience_points_tamed_dinos)
    elif experience_type == "joueurs":
        result += generate_section("LevelExperienceRampOverrides", experience_points_players)

    return result

def generate_section(section_name, experience_points):
    section = f"{section_name}=(ExperiencePointsForLevel[0]={experience_points[0]}"
    for i in range(1, len(experience_points)):
        section += f",ExperiencePointsForLevel[{i}]={experience_points[i]}"
    section += ")\n"
    return section
