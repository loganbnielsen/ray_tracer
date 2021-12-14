from assets.Asset import Asset
from assets.Polygon import Polygon
from helpers.Methods import reflection_ray
import numpy as np

class Cube(Asset):
    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z, diffuse_color, specular_color, reflectivity, refractivity, material,
                 glossy_jf=0, translucency_jf=0):
        super().__init__(diffuse_color, specular_color, reflectivity, refractivity, material, glossy_jf, translucency_jf)
        FRONT = [np.array([min_x, min_y, min_z]),
                 np.array([min_x, min_y, max_z]),
                 np.array([max_x, min_y, max_z]),
                 np.array([max_x, min_y, min_z])]
        LEFT = [np.array([min_x, min_y, min_z]),
                np.array([min_x, max_y, min_z]),
                np.array([min_x, max_y, max_z]),
                np.array([min_x, min_y, max_z])]
        BOTTOM = [np.array([min_x, min_y, min_z]),
                  np.array([min_x, max_y, min_z]),
                  np.array([max_x, max_y, min_z]),
                  np.array([max_x, min_y, min_z])]
        BACK = [np.array([max_x, max_y, max_z]),
                np.array([min_x, max_y, max_z]),
                np.array([min_x, max_y, min_z]),
                np.array([max_x, max_y, min_z])]
        RIGHT = [np.array([max_x, max_y, max_z]),
                 np.array([max_x, max_y, min_z]),
                 np.array([max_x, min_y, min_z]),
                 np.array([max_x, min_y, max_z])]
        TOP = [np.array([max_x, max_y, max_z]),
               np.array([max_x, min_y, max_z]),
               np.array([min_x, min_y, max_z]),
               np.array([min_x, max_y, max_z])]
        self._set_min_coords(np.row_stack([*FRONT, *LEFT, *BOTTOM, *BACK, *RIGHT, *TOP]))
        self.faces = [Polygon(face, diffuse_color, specular_color, reflectivity, refractivity, material, glossy_jf, translucency_jf)
                      for face in [FRONT, LEFT, BOTTOM, BACK, RIGHT, TOP]]
        self.closest_face = None # cache the closest face

    def _set_min_coords(self, coords):
        self.min_x, self.min_y, self.min_z = coords.min(0)
        self.max_x, self.max_y, self.max_z = coords.max(0)


    def intersect(self, origin, ray):
        closest_t = None
        for face in self.faces:
                t = face.intersect(origin, ray)
                if t:
                    if closest_t:
                        if t < closest_t:
                            closest_t = t
                            self.closest_face = face
                    else:
                        closest_t = t
                        self.closest_face = face
        return closest_t
    
    def normal(self, intersect_loc):
        return self.closest_face.normal(intersect_loc)

    def __str__(self):
        _str = ",".join([str(f) for f in self.faces])
        return "[ Cube: "+_str+ " ]"
                                
