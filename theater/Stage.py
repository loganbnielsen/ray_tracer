import numpy as np
from assets import Asset
from abstract.Intersection import Intersection
from helpers.Methods import offset_vector

class Stage:
    # objects: list[Asset]
    # lights: list[BaseLight]

    def __init__(self, objects, directional_lights):
        self.objects = objects
        self.directional_lights = directional_lights
    
    def find_closest_intersection(self, origin, ray):
        """
            returns (nearest_object, location_of_intersection)
        """
        offset_origin = offset_vector(origin, ray)
        smallest_dist = np.inf
        closest_intersection = None
        for obj in self.objects: 
            dist = obj.intersect(offset_origin, ray)
                            
            if dist and dist < smallest_dist: # check that intersected and if it's the closest intersection
                smallest_dist = dist
                intersect_loc = offset_origin + ray * dist # record point in space
                closest_intersection = Intersection(obj, intersect_loc, ray, dist) 
        return closest_intersection             
