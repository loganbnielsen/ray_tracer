import numpy as np
from assets.Sphere import Sphere
from assets.Triangle import Triangle
from equipment.lights.DirectionalLightSource import DirectionalLightSource

# # objects in the scene (x,y,z)
# objects = [
#     Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1),
#     Sphere( np.array([-1, -2, 11]), 1, "RED", "WHITE", 0.1, 0.5, "air", 1),
#     Sphere( np.array([ 2, -2, 10]), 1, "GREEN", "WHITE", 0.1, 0.5, "air", 1),
#     Sphere( np.array([ -1.75, -2, 9]), 1, "WHITE", "WHITE", 0.1, .95, "air", 1),
#     Sphere( np.array([ 2, -2, 8]), 1, "WHITE", "WHITE", 0.1, .95, "air", 1),
#     Triangle( np.array([-3,-2, 14]), np.array([3,-2,14]), np.array([0,1,14]), "DARK_GRAY", "WHITE", 0.1, 0, None, 1)
# ]

objects = [
    Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1),
    Sphere( np.array([ 3, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1)
]

# light sources (does not include ambient lighting)
# see phong illumination for that
directional_lights = [
    # DirectionalLightSource( np.array([0.5,-1,1]), "WHITE", 1),
    DirectionalLightSource( np.array([.5,-2,-1]), "WHITE", 1)
]