from assets import Asset
from helpers.Methods import reflection_ray
import numpy as np

class Intersection:
    def __init__(self, obj:Asset, intersect_loc, intersect_ray, dist):
        """
            obj: the object that was intersected
            intersect_loc: the location in space the intersection occured
            intersect_ray: the ray that his the object (points INTO the intersection)
        """
        self.obj = obj
        self.loc = intersect_loc
        self.ray = intersect_ray
        self.t = dist
        # generated when needed (expensive)
        self._normal = self._get_normal()
        self._reflection = reflection_ray(-self.ray, self.normal())

    def _get_normal(self):
        normal = self.obj.normal(self.loc)
        if np.dot(self.ray, normal) > 0: # check direction (remember ray points INTO the intersection)
            normal *= -1
        return normal

    def normal(self):
        return self._normal

    def reflection(self):
        return self._reflection