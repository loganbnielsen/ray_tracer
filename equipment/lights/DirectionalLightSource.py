from equipment.lights.BaseLight import BaseLight
import numpy as np
from theater.Stage import Stage
from helpers.Methods import offset_vector

class DirectionalLightSource(BaseLight):
    def __init__(self, light_direction, color):
        super().__init__(color)
        self.light_direction = light_direction / np.linalg.norm(light_direction)
        self.direction_to_source = -self.light_direction # always the case for directional light sources

    def is_visible(self, point, stage:Stage):
        offset_origin = offset_vector(point, self.direction_to_source)
        intersect = stage.find_closest_intersection\
                        (offset_origin, self.direction_to_source)
        return False if intersect else True
