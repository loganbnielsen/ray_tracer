from config.Colors import color_rgb_map

shadow_factor = 0.5 # 0 implies no blocked our light. 1 implies all light blocked out

phong_illumination_constants = {
    'k_a': 0.2, # ambient constant
    'k_d': 0.9, # diffuse constant
    'k_s': 2, # specular constant
    'I_a_name': 'WHITE', # ambient light color
    'p': 50
}