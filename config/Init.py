import numpy as np
from assets.Sphere import Sphere
from equipment.lights.DirectionalLightSource import DirectionalLightSource
from config.Colors import color_rgb_map

class CameraPosition:
    x = 0
    y = .5
    z = -1

class ScreenSize:
    height = 3*100
    width = 3*150

background_color = color_rgb_map["WHITE"] 

# objects in the scene
objects = [
    Sphere( np.array([ 1, -2, 8]), 1, "BLUE", "WHITE"),
    Sphere( np.array([-2, -2, 5]), 1, "RED", "WHITE")
]

# light sources (does not include ambient lighting)
directional_lights = [
    DirectionalLightSource( np.array([0.5,-1,1]), "WHITE")
]