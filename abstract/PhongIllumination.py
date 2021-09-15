from abstract.Intersection import Intersection
from theater.Stage import Stage
from config.Colors import color_rgb_map
from helpers.Methods import reflection_ray

import numpy as np

class PhongIllumination:
    def __init__(self, k_a, k_d, k_s, I_a_name, p):
        self.k_a = k_a
        self.k_d = k_d 
        self.k_s = k_s
        self.I_a = color_rgb_map[I_a_name]
        self.p = p

    def run(self, intersect:Intersection, stage: Stage):
        ambient_term = self.k_a * self.I_a * intersect.obj.diffuse_color
        sum_over_lights = self._sum_over_lights(intersect, stage)
        return np.clip(ambient_term + sum_over_lights, 0, 1)

    def _sum_over_lights(self, intersect:Intersection, stage:Stage):
        result = np.array([0,0,0])
        # directional lighting
        for light in stage.directional_lights:
            if light.is_visible(intersect.loc, stage):
                N = intersect.normal()
                R = reflection_ray(light.direction_to_source, N) # light reflection
                # diffuse calculation
                diffuse = self.k_d *\
                          intersect.obj.diffuse_color *\
                          max(0, np.dot(N, light.direction_to_source))
                # specular calculation
                specular = self.k_s *\
                           intersect.obj.specular_color *\
                           max(0, np.dot(-intersect.ray, R)) ** self.p
                result = result + light.color * (diffuse + specular)
        return result