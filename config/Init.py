import numpy as np
from assets.Sphere import Sphere
from assets.Triangle import Triangle
from equipment.lights.DirectionalLightSource import DirectionalLightSource
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
is_dry_run = False # no illumination model, no reflections, no refractions, simply diffuse color
is_run_illumination = True # include illumination model
is_run_reflection = True
is_run_refraction = True

background_color = color_rgb_map["LIGHT_GRAY"] 

# objects in the scene (x,y,z)
objects = [
    Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water"),
    Sphere( np.array([-1, -2, 11]), 1, "RED", "WHITE", 0.1, 0.5, "air"),
    Sphere( np.array([ 2, -2, 10]), 1, "GREEN", "WHITE", 0.1, 0.5, "air"),
    Sphere( np.array([ -1.75, -2, 9]), 1, "WHITE", "WHITE", 0.1, .95, "air"),
    Sphere( np.array([ 2, -2, 8]), 1, "WHITE", "WHITE", 0.1, .95, "air"),
    Triangle( np.array([-3,-2, 14]), np.array([3,-2,14]), np.array([0,1,14]), "DARK_GRAY", "WHITE", 0.1, 0, None)
]

# light sources (does not include ambient lighting)
# see phong illumination for that
directional_lights = [
    # DirectionalLightSource( np.array([0.5,-1,1]), "WHITE", 1),
    DirectionalLightSource( np.array([.5,-2,-1]), "WHITE", 1)
]