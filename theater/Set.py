from equipment.Camera import Camera
from equipment.Screen import Screen
from theater.Stage import Stage

import numpy as np

class Set:
    camera: Camera
    screen: Screen
    stage: Stage

    def __init__(self, camera:Camera, screen:Screen, stage:Stage):
        self.camera = camera
        self.screen = screen
        self.stage = stage
    
    def process_ray(self, ray):
        closest_obj, intersect_loc = self.stage.find_nearest_object\
            (self.camera.position, ray)
        if closest_obj:
            color = closest_obj.color
            reflection_ray = self.reflection_ray(intersect_loc, ray, closest_obj)
            # TODO use reflection_ray
            return color * \
                self.cumulative_light_factor(intersect_loc)

    ##########3

    def reflection_ray(self, intersect_loc, ray, obj):
        normal = obj.normal(intersect_loc)
        reflection = ray - 2 * np.linalg.dot(normal, ray) * normal
        return reflection
    
    def cumulative_light_factor(self, loc):
        cumulative_light_factor = 1
        # directional lights
        for light in self.stage.directional_lights:
            cumulative_light_factor *=\
                light.visibility(loc, self.stage)
        # add other light sources
        return cumulative_light_factor


