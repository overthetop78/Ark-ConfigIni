# File: functions/generate_engram_points.py

def generate_engram_points(start_points, levels_to_unlock_all, increment_type, num_levels, max_points=None, levels_increment=None):
    engram_points = []
    current_points = start_points

    if increment_type == "linear":
        for _ in range(num_levels):
            engram_points.append(start_points)

    elif increment_type == "incremental":
        if max_points is None or levels_increment is None:
            raise ValueError("max_points et levels_increment doivent être définis pour l'incrémentation.")
        
        increment_value = (max_points - start_points) // ((num_levels - 1) // levels_increment)
        while len(engram_points) < num_levels:
            for _ in range(levels_increment):
                engram_points.append(current_points)
                if len(engram_points) >= num_levels:
                    break
            current_points += increment_value

    elif increment_type == "exponential":
        if max_points is None or levels_increment is None:
            raise ValueError("max_points et levels_increment doivent être définis pour l'incrémentation exponentielle.")
        
        factor = (max_points / start_points) ** (1 / (levels_to_unlock_all - 1))
        for level in range(num_levels):
            current_points = start_points * (factor ** level)
            engram_points.append(int(current_points))

    return engram_points

def generate_override_engram_points(engram_points):
    result = ""
    for points in engram_points:
        result += f"OverridePlayerLevelEngramPoints={points}\n"
    return result

def generate_max_experience_points(players_experience, dinos_experience):
    max_player_exp = players_experience[-1] if players_experience else 0
    max_dino_exp = dinos_experience[-1] if dinos_experience else 0
    result = f"OverrideMaxExperiencePointsPlayer={max_player_exp}\n"
    result += f"OverrideMaxExperiencePointsDino={max_dino_exp}\n"
    return result
