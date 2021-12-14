from abstract.Intersection import Intersection
from theater.Stage import Stage
from config.Colors import color_rgb_map
from helpers.Methods import reflection_ray
from equipment.lights import BaseLight

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
        avg_over_lights = self._avg_over_lights(intersect, stage)
        return np.clip(ambient_term + avg_over_lights, 0, 1)

    def _avg_over_lights(self, intersect:Intersection, stage:Stage):
        results = []
        # directional lighting
        for light in stage.directional_lights:
            vis_factor = light.visibility(intersect.loc, stage)
            results.append( self._light_calculations(intersect, vis_factor, light, light.direction_to_source) )
        # area lighting (TODO could put these all together but harder to debug)
        for light in stage.area_lights:
            vis_factor, direction_to_source = light.visibility(intersect.loc, stage)
            results.append( self._light_calculations(intersect, vis_factor, light, direction_to_source) ) # TODO direction is a kluge. Needs serious refactoring.
        if len(results) > 0:
            return np.row_stack(results).mean(0)
        else:
            return np.zeros(3)

    def _light_calculations(self, intersect:Intersection, vis_factor: float, light:BaseLight, direction_to_source:np.array):
        if vis_factor != 0:
            N = intersect.normal()
            R = reflection_ray(direction_to_source, N) # light reflection
            # diffuse calculation
            diffuse = self.k_d *\
                        intersect.obj.diffuse_color *\
                        max(0, np.dot(N, direction_to_source))
            # specular calculation
            specular = self.k_s *\
                        intersect.obj.specular_color *\
                        max(0, np.dot(-intersect.ray, R)) ** self.p
            return vis_factor * light.intensity * light.color * (diffuse + specular)
        else:
            return np.zeros(3)
