import numpy as np
from assets.Asset import Asset
from assets.Cube import Cube
from abstract.Intersection import Intersection
from helpers.Methods import offset_vector
from algo.BoundingBox import BoundingBoxSplit, Box
from config.Settings import bounding_box_configs

class Stage:
    # objects: list[Asset]
    # lights: list[BaseLight]
    
    # TODO use bounding box algo to store objects
    # and intersect against the bounding boxes to
    # find closest objects

    def __init__(self, objects, directional_lights):
        self.objects = objects
        self.directional_lights = directional_lights
        self.stored_in_boxes = False
        # place objects in boxes
        # bbs = BoundingBoxSplit(15, 15)
        bbs = BoundingBoxSplit(**bounding_box_configs)
        boxes = bbs.fit(self.objects)
        if len(boxes) > 1:
            print("STORED IN BOUNDING BOX")
            # TODO convert boxes into something that can be intersected against (make a box an Asset)
            self.boxes = boxes
            self.box_intersectables = [Cube(box.min_x, box.max_x, box.min_y, box.max_y, box.min_z, box.max_z, None, None, None, None, None, None)
                                       for box in self.boxes]
            self.stored_in_boxes = True
        else:
            print(f"NOT STORED IN BOXES. {boxes}")
    
    def find_closest_intersection(self, origin, ray):
        """
            returns (nearest_object, location_of_intersection)
        """
        offset_origin = offset_vector(origin, ray)
        smallest_dist = np.inf
        closest_intersection = None
        if not self.stored_in_boxes:
            for obj in self.objects: 
                dist = obj.intersect(offset_origin, ray)
                if dist and dist < smallest_dist: # check that intersected and if it's the closest intersection
                    smallest_dist = dist
                    intersect_loc = offset_origin + ray * dist # record point in space
                    closest_intersection = Intersection(obj, intersect_loc, ray, dist) 
        else:
            for i, intersectable in enumerate(self.box_intersectables):
                if intersectable.intersect(offset_origin, ray):
                    for obj in self.boxes[i].items:
                        dist = obj.intersect(offset_origin, ray)
                        if dist and dist < smallest_dist:
                            smallest_dist = dist
                            intersect_loc = offset_origin + ray * dist
                            closest_intersection = Intersection(obj, intersect_loc, ray, dist)
        return closest_intersection
            


