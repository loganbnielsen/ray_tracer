from equipment.Camera import Camera
from equipment.Screen import Screen
from theater.Stage import Stage
from theater.Set import Set

from helpers.Methods import camera_rays_generator
from abstract.Intersection import Intersection
from abstract.PhongIllumination import PhongIllumination
from config.Init import background_color

import numpy as np

class RayTracer:
    def __init__(self, _set: Set, illumination_model: PhongIllumination):
        self.camera = _set.camera
        self.screen = _set.screen
        self.stage  = _set.stage
        self.illumination_model = illumination_model

    def run(self):
        for i, j, ray in camera_rays_generator(self.camera, self.screen):
            self.screen.grid.colors[i,j] = self._gen_color(self.camera.position, ray)

    def _gen_color(self, origin, ray):
        closest_intersect = self.stage.find_closest_intersection(origin, ray)
        if closest_intersect:
            color = self.illumination_model.run(
                closest_intersect,
                self.stage
            )
        else:
            color = background_color
        return color