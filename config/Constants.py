from config.Colors import color_rgb_map

phong_illumination_constants = {
    'k_a': 0.2, # ambient constant
    'k_d': 0.9, # diffuse constant
    'k_s': 2, # specular constant
    'I_a_name': 'WHITE', # ambient light color
    'p': 50
}

EPSILON = 1e-7

index_of_refraction = {
    'air': 1,
    'water': 1.33,
    'glass': 1.50,
    'diamond': 2.417
}