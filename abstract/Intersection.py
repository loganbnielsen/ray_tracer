from assets import Asset
from helpers.Methods import reflection_ray

class Intersection:
    def __init__(self, obj:Asset, intersect_loc, intersect_ray):
        """
            obj: the object that was intersected
            intersect_loc: the location in space the intersection occured
            intersect_ray: the ray that his the object (points INTO the intersection)
        """
        self.obj = obj
        self.loc = intersect_loc
        self.ray = intersect_ray
        # generated when needed (expensive)
        self._normal = self.obj.normal(self.loc)
        self._reflection = reflection_ray(-self.ray, self.normal())

    def normal(self):
        return self._normal

    def reflection(self):
        return self._reflection