import numpy as np

from assets import Asset


class BoundingBoxSplit:
    def __init__(self, box_size, max_depth):
        """
            A box has 6 faces. A naive algo will need to intersect 5 faces to
            determine if the ray passes through the box (typically, a ray will intersect
            a box twice if it hits the box).
            Each side of the box is composed of 2 triangles that can be intersected against.
            Therefore there are 10 intersection tests that will be conducted.
            Because of this, box_size should be greater than 10 for there to be any performance
            increase from using this method.
        """
        self.box_size = box_size  # stops splitting once box holds this many items or less
        self.max_depth = max_depth

    def fit(self, objects:[Asset]):
        # prep first box
        boxes = [self._init_box(objects)]
        return self._recursive_split(boxes, nsplits=0)

    def _init_box(self, objects:[Asset]):
        x_min = y_min = z_min = -np.inf
        x_max = y_max = z_max =  np.inf
        for obj in objects:
            x_min = min(x_min, obj.x_min)
            y_min = min(y_min, obj.y_min)
            z_min = min(z_min, obj.z_min)

            x_max = max(x_max, obj.x_max)
            y_max = max(y_max, obj.y_max)
            z_max = max(z_max, obj.z_max)
        return Box(x_min, y_min, z_min, x_max, y_max, z_max, objects)
    
    def _recursive_split(self, boxes:[Box], nsplits):
        if nsplits >= self.max_depth:
            return boxes
        else:
            boxes = []
            for box in boxes:
                if len(box.items) <= self.box_size: # box has few enough items
                    boxes.append(box)
                else: # box has too many items
                    box_splits = box.split_box()
                    for sbox in box_splits:
                        if len(sbox) > 0:
                            boxes.append(sbox)
            boxes = [sbox for box in boxes for sbox in box.split_box() if len(sbox) > 0]
            return self._recursive_split(boxes, nsplits+1)

class Box:
    items: [Asset]

    def __init__(self, min_x, min_y, min_z, max_x, max_y, max_z, items:[Asset]):
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z

        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z

        self.items = items

    def _x_split(self):
        new_x = (self.min_x + self.max_x)/2
        # already known that y and z are within bounds,
        # we want to know which side each object is on (can be on both)
        box1 = []
        box2 = []
        for obj in self.items:
            if obj.x_min <= new_x: # box starts from "bottom" so item is in box iff the bottom of the item is in it
                box1.append(obj)
            if new_x <= obj.x_max: # box starts from "top" so item is in the box iff the top of the item is in it
                box2.append(obj)
        return [box1, box2], abs(len(box1) - len(box2))

    def _y_split(self):
        new_y = (self.min_y + self.max_y)/2
        box1 = []
        box2 = []
        for obj in self.items:
            if obj.y_min <= new_y:
                box1.append(obj)
            if new_y <= obj.y_max:
                box2.append(obj)
        return [box1, box2], abs(len(box1) - len(box2))

    def _z_split(self):
        new_z = (self.min_z + self.max_z)/2
        box1 = []
        box2 = []
        for obj in self.items:
            if obj.z_min <= new_z:
                box1.append(obj)
            if new_z <= obj.z_max:
                box2.append(obj)
        return [box1, box2], abs(len(box1) - len(box2))

    def split_box(self):
        """
            box splits are done with a median axis split by default
        """
        xboxes, xdif = self._x_split()
        # set these as best split so far
        best_split  = xboxes
        largest_dif = xdif
        # test other splits
        yboxes, ydif = self._y_split()
        if ydif > largest_dif:
            best_split = yboxes
            largest_dif = ydif 
        zboxes, zdif = self._z_split()
        if zdif > largest_dif:
            best_split = zboxes
            largest_dif = zdif
        return best_split