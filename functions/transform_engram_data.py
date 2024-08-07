def transform_engram_data_to_override_format(engram_data):
    override_entries = []

    for engram in engram_data:
        engram_class_name = engram['name']
        engram_hidden = str(engram['hidden']).lower()
        engram_points_cost = engram['points']
        engram_level_requirement = engram['level']
        remove_engram_prereq = str(not engram['requires_prereq']).lower()
        
        formatted_entry = (f'OverrideNamedEngramEntries=(EngramClassName="{engram_class_name}",'
                           f'EngramHidden={engram_hidden},'
                           f'EngramPointsCost={engram_points_cost},'
                           f'EngramLevelRequirement={engram_level_requirement},'
                           f'RemoveEngramPreReq={remove_engram_prereq})')
        override_entries.append(formatted_entry)

    return override_entries

# Exemple d'utilisation
if __name__ == "__main__":
    from constants.engram_const import ENGRAMS
    engram_data = ENGRAMS.copy()
    override_entries = transform_engram_data_to_override_format(engram_data)
    for entry in override_entries:
        print(entry)
