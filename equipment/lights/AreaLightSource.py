from equipment.lights.BaseLight import BaseLight
import numpy as np
from assets.Triangle import Triangle
from theater.Stage import Stage
from helpers.Methods import offset_vector, jitter_array, euclid_length
from algo.EarClipper import EarClipper

class AreaLightSource(BaseLight):
    def __init__(self, vertices, color, intensity):
        """
            vertices should define a flat surface
        """
        super().__init__(color)
        self.intensity = intensity

        list_triangle_coords = EarClipper().clip(vertices)
        self.triangles = [Triangle(vtx0, vtx1, vtx2, None, None, None, None, None, None, None)
                          for vtx0, vtx1, vtx2 in list_triangle_coords]
        coords = np.row_stack(list_triangle_coords)
        self.min_x, self.min_y, self.min_z = coords.min(0)
        self.max_x, self.max_y, self.max_z = coords.max(0)
        self.center = np.array([(self.max_x + self.min_x)/2, (self.max_y + self.min_y)/2, (self.max_z + self.min_z)/2])
        
    
    def visibility(self, point, stage:Stage):
        ntests=10 # VERY COMPUTATIONALLY EXPENSIVE
        # init random sample
        x = np.random.uniform(self.min_x,self.max_x,ntests)
        y = np.random.uniform(self.min_y,self.max_y,ntests)
        z = np.random.uniform(self.min_z,self.max_z,ntests)
        tests = np.column_stack([x,y,z])
        # find which percentage get passed
        nsuccess = 0
        for light_source in tests:
            dir_to_light = light_source - point
            dir_to_light = dir_to_light / euclid_length(dir_to_light)
            offset_origin = offset_vector(point, dir_to_light)
            intersect = stage.find_closest_intersection(offset_origin, dir_to_light)
            if not intersect: # not occluded
                nsuccess += 1
        direction_to_source = self.center - point
        direction_to_source = direction_to_source / euclid_length(direction_to_source)
        return nsuccess/ntests, direction_to_source


