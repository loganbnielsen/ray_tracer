import numpy as np
from assets.Asset import Asset
from helpers.Methods import offset_vector, euclid_length

class Sphere(Asset):
    def __init__(self, center, radius, diffuse_color, specular_color, reflectivity, refractivity, material, jitter_factor):
        super().__init__(diffuse_color, specular_color, reflectivity, refractivity, material, jitter_factor)
        self.center = center
        self.radius = radius
        self._set_min_coords()

    def _set_min_coords(self):
        self.min_x, self.min_y, self.min_z = self.center - self.radius # this point doesn't exist but each coordinate magnitude exists exactly once and it's the min
        self.max_x, self.max_y, self.max_z = self.center + self.radius # this point doesn't exist but each coordinate magnitude exists exactly once and it's the max
    
    def intersect(self, origin, ray):
        # https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9
        offset_origin = offset_vector(origin, ray)
        b = 2 * np.dot(ray, offset_origin - self.center)
        c = euclid_length(offset_origin - self.center)**2 - self.radius**2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
            elif t1 > 0 and t2 < 0:
                return t1
            elif t1 < 0 and t2 > 0:
                return t2
            else:
                # both are negative
                pass 
    
    def normal(self, intersect_loc):
        v = intersect_loc - self.center
        u_v = v / euclid_length(v)
        return u_v
