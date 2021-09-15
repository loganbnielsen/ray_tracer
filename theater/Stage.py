import numpy as np
from assets import Asset
from abstract.Intersection import Intersection

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
        smallest_dist = np.inf
        closest_intersection = None
        for obj in self.objects: 
            dist = obj.intersect(origin, ray)
            if dist and dist < smallest_dist: # check that intersected and if it's the closest intersection
                intersect_loc = origin + ray * dist # record point in space
                closest_intersection = Intersection(obj, intersect_loc, ray) 
        return closest_intersection             
