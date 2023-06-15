singers = {
    "JLEE": 10,
    "JTAN": 12,
    "KENN": 9,
    "MCUR": 1,
    "MPOL": 2,
    "MPUR": 5,
    "NJAT": 4,
    "PMAR": 6,
    "SAMF": 11,
    "VKOW": 7,
    "ZHIY": 8
}

part_codes = {
    1: "Soprano",
    2: "Soprano",
    3: "Soprano",
    4: "Alto",
    5: "Alto",
    6: "Alto",
    7: "Tenor",
    8: "Tenor",
    9: "Baritone",
    10: "Baritone",
    11: "Baritone",
    12: "Bass"
}

def get_singer_part(singer_name):
    singer_name = singer_name.upper()

    if singer_name in singers:
        code = singers[singer_name]
        part = part_codes[code]
        return part
    else:
        return None
    
def part_to_shift(ori_spk_part, tar_spk_part):
    shift_table = {
        'Bass': {'Bass': 0, 'Baritone': 4, 'Tenor': 8, 'Alto': 12, 'Soprano': 12},
        'Baritone': {'Bass': -4, 'Baritone': 0, 'Tenor': 4, 'Alto': 8, 'Soprano': 8},
        'Tenor': {'Bass': -8, 'Baritone': -4, 'Tenor': 0, 'Alto': 4, 'Soprano': 8},
        'Alto': {'Bass': -12, 'Baritone': -8, 'Tenor': -4, 'Alto': 0, 'Soprano': 4},
        'Soprano': {'Bass': -12, 'Baritone': -8, 'Tenor': -4, 'Alto': -4, 'Soprano': 0}
    }
    
    if ori_spk_part not in shift_table or tar_spk_part not in shift_table:
        return "Invalid parts provided."
    
    shift = shift_table[ori_spk_part][tar_spk_part]
    
    return shift

def singer_shift(nus_name, m4_name):
    ori_spk_part = get_singer_part(nus_name)
    tar_spk_part = m4_name
    
    if ori_spk_part is None or tar_spk_part is None:
        return "Invalid singer name provided."
    
    shift = part_to_shift(ori_spk_part, tar_spk_part)
    
    return shift
    

