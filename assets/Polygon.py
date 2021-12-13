import numpy as np
from assets.Asset import Asset
from assets.Triangle import Triangle
from helpers.Methods import offset_vector, euclid_length
from config.Constants import EPSILON
from algo.EarClipper import EarClipper

class Polygon(Asset):
    def __init__(self, vertices:[np.array], diffuse_color, specular_color, reflectivity, refractivity, material,
                 glossy_jf, translucency_jf):
        """
            Note that a polygon is a flat object.
            Don't use this for something 3D
        """
        super().__init__(diffuse_color, specular_color, reflectivity, refractivity, material, glossy_jf, translucency_jf)
        list_triangle_coords = EarClipper().clip(vertices)
        self.triangles = [Triangle(vtx0, vtx1, vtx2, diffuse_color, specular_color, reflectivity,
                                      refractivity, material, jitter_factor)
                          for vtx0, vtx1, vtx2 in list_triangle_coords]
        self.closest_intersected_triangle = None # for caching intersections
        self._set_min_coords(np.row_stack([item for l in list_triangle_coords for item in l]))

    def _set_min_coords(self, coords):
        self.min_x, self.min_y, self.min_z = coords.min(0)
        self.max_x, self.max_y, self.max_z = coords.max(0)
    
    def intersect(self, origin, ray):
        closest_t = None
        for triangle in self.triangles:
            t = triangle.intersect(origin, ray)
            if t:
                if closest_t:
                    if t < closest_t:
                        closest_t = t
                        self.closest_intersected_triangle
                else:
                    closest_t = t 
                    self.closest_intersected_triangle
        return closest_t
    
    def normal(self, intersect_loc):
        return self.closest_intersected_triangle.normal(intersect_loc)
            
    
