from config.Colors import color_rgb_map

class CameraPosition:
    x = 0
    y = .5
    z = -3

class ScreenSize:
    m = 3
    height = m*100
    width = m*150
    samples_per_pixel = 4 # 1, 4, 9, 16, .... n^2


max_parent_rays = 5
is_dry_run = False # if true, no illumination model, no reflections, no refractions, simply diffuse color
is_run_illumination = True # include illumination model
is_run_reflection = True
is_run_refraction = True

background_color = color_rgb_map["SKY_BLUE"] 

jitter_factor = 0.0001

bounding_box_configs = {
    "box_size": 11, # maximum boxes
    "max_depth": 3 # number of splits allowed
}