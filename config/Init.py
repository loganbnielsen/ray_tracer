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
    height = 3*100
    width = 3*150

max_parent_rays = 2
is_dry_run = False # no illumination model, no reflections, no refractions, simply diffuse color
is_run_illumination = True # include illumination model
is_run_reflection = True
is_run_refraction = True

background_color = color_rgb_map["WHITE"] 

# objects in the scene (x,y,z)
objects = [
    # Sphere( np.array([ 0.5, -2, 16]), 1, "BLUE", "WHITE", 0.1),
    # Sphere( np.array([-2, -2, 14]), 1, "RED", "WHITE", 0.1),
    # Sphere( np.array([ 2, -2, 10]), 1, "GREEN", "WHITE", 0.1),
    Sphere(  np.array([0,-1,5]), 1, "BLUE", "WHITE", 0, 0, None),
    Triangle( np.array([-2,-2,10]), np.array([2,-2,10]), np.array([0,1,10]), "LIGHT_GRAY", "WHITE", 0.1, 0, None)
]

# light sources (does not include ambient lighting)
# see phong illumination for that
directional_lights = [
    DirectionalLightSource( np.array([0.5,-1,1]), "WHITE")
]