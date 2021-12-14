import numpy as np
from assets.Sphere import Sphere
from assets.Triangle import Triangle
from assets.Polygon import Polygon
from assets.Cube import Cube
from equipment.lights.DirectionalLightSource import DirectionalLightSource
from equipment.lights.AreaLightSource import AreaLightSource

# # objects in the scene (x,y,z)
objects = [
    Sphere( np.array([ 0.25, -2, 12.5]), 1, "BLUE", "WHITE", 0.2, 0.00, "air", 1, 1),
    Sphere( np.array([-2, -2, 11]), 1, "RED", "WHITE", 0.2, 0.00, "air", 1, 1),
    # Sphere( np.array([ 2, -2, 9]), 1, "GREEN", "WHITE", 0.2, 0.00, "air", 1, 1),
    Cube(1.5, 3, -3, -1.5, 8.5, 10, "GREEN", "WHITE", 0.2, 0.00, "air", 1, 1),
    # Cube(-3,-1,-1,1,13,15,"DARK_GRAY","WHITE",.1,0, None,1,1),
    # Sphere( np.array([ -1.75, -2, 9]), 1, "WHITE", "WHITE", 0.1, .95, "air", 1, 1),
    # Sphere( np.array([ 2, -2, 8]), 1, "WHITE", "WHITE", 0.1, .95, "air", 1, 1),
    # Triangle( np.array([-3,-2, 14]), np.array([3,-2,14]), np.array([0,1,14]), "DARK_GRAY", "WHITE", 0.1, 0, None, 1, 1),
    Polygon( [np.array([-100,-3,-50]),np.array([100,-3,-50]),np.array([100,-3,50]),np.array([-100,-3,50])], "LIGHT_GRAY", "LIGHT_GRAY", 0, 0, None, 0, 0)
]

# objects = [
#     Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1, 1),
#     Sphere( np.array([ 3, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1, 1)
# ]

# light sources (does not include ambient lighting)
# see phong illumination for that
directional_lights = [
    # DirectionalLightSource( np.array([0.5,-1,1]), "WHITE", 1),
    # DirectionalLightSource( np.array([.5,-2,-1]), "WHITE", 1),
    # DirectionalLightSource( np.array([.5,-.1,1]), "WHITE", 1)
]

area_lights = [
    AreaLightSource([
        np.array([-3, 1, 4]),
        np.array([-1, 1, 4]),
        np.array([-1, 1, 2]),
        np.array([-3, 1, 2]),
    ], "WHITE", 1)
]