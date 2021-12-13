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
        x_min = y_min = z_min =  np.inf
        x_max = y_max = z_max = -np.inf
        for obj in objects:
            x_min = min(x_min, obj.min_x)
            y_min = min(y_min, obj.min_y)
            z_min = min(z_min, obj.min_z)

            x_max = max(x_max, obj.max_x)
            y_max = max(y_max, obj.max_y)
            z_max = max(z_max, obj.max_z)
        return Box(x_min, y_min, z_min, x_max, y_max, z_max, objects)
    
    def _recursive_split(self, boxes, nsplits): # TODO optimize this
        if nsplits >= self.max_depth:
            return boxes
        else:
            changed = False
            new_boxes = []
            for box in boxes:
                if len(box.items) <= self.box_size: # box has few enough items
                    new_boxes.append(box)
                else: # box has too many items, split it
                    box_splits, is_same = box.split_box()
                    if not is_same:
                        changed = True
                        for sbox in box_splits:
                            if len(sbox) > 0: # keep non-empty boxes
                                new_boxes.append(sbox)
                    else:
                        new_boxes.append(box_splits[0])
            if changed:
                return self._recursive_split(new_boxes, nsplits+1)
            else:
                return boxes

class Box:
    items: [Asset]

    def __init__(self, min_x=np.inf, min_y=np.inf, min_z=np.inf, max_x=-np.inf, max_y=-np.inf, max_z=-np.inf, items:[Asset] = list()):
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z

        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z

        self.items = items

    def insert(self, obj: Asset):
        self.min_x = min(self.min_x, obj.min_x)
        self.min_y = min(self.min_y, obj.min_y)
        self.min_z = min(self.min_z, obj.min_z)

        self.max_x = max(self.max_x, obj.max_x)
        self.max_y = max(self.max_y, obj.max_y)
        self.max_z = max(self.max_z, obj.max_z)

        self.items.append(obj)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Box: min_x={self.min_x},min_y={self.min_y},min_z={self.min_z},max_x={self.max_x},max_y={self.max_y},max_z={self.max_z},n_items={len(self.items)}."

    """
        TODO make these three functions into one function
    """
    def _x_split(self):
        new_x = (self.min_x + self.max_x)/2
        # already known that y and z are within bounds,
        # we want to know which side each object is on (can be on both)
        box1 = Box()
        box1.items = list()
        box2 = Box()
        box2.items = list()
        same = False
        for obj in self.items:
            in_first = in_second = False
            if obj.min_x <= new_x: # box starts from "bottom" so item is in box iff the bottom of the item is in it
                box1.insert(obj)
                in_first = True
            if new_x <= obj.max_x: # box starts from "top" so item is in the box iff the top of the item is in it
                box2.insert(obj)
                in_second = True
            if in_first and in_second:
                pass
            else:
                same = False
        return [box1, box2], np.std([len(box1), len(box2)]), same

    def _y_split(self):
        new_y = (self.min_y + self.max_y)/2
        box1 = Box()
        box1.items = list()
        box2 = Box()
        box2.items = list()
        same = False
        for obj in self.items:
            in_first = in_second = False
            if obj.min_y <= new_y:
                box1.insert(obj)
                in_first = True
            if new_y <= obj.max_y:
                box2.insert(obj)
                in_second = True
            if in_first and in_second:
                pass
            else:
                same = False
        return [box1, box2], np.std([len(box1), len(box2)]), same

    def _z_split(self):
        new_z = (self.min_z + self.max_z)/2
        box1 = Box()
        box1.items = list()
        box2 = Box()
        box2.items = list()
        same = False
        for obj in self.items:
            in_first = in_second = False
            if obj.min_z <= new_z:
                box1.insert(obj)
                in_first = True
            if new_z <= obj.max_z:
                box2.insert(obj)
                in_second = True
            if in_first and in_second:
                pass
            else:
                same = False
        return [box1, box2], np.std([len(box1), len(box2)]), same

    def split_box(self):
        """
            box splits are done with a median axis split by default
        """
        is_same = True
        xboxes, xdif, same = self._x_split()
        if not same:
            is_same = False
        # set these as best split so far
        best_split  = xboxes
        largest_dif = xdif
        # test other splits
        yboxes, ydif, same = self._y_split()
        if not same:
            is_same = False
            if ydif > largest_dif:
                best_split = yboxes
                largest_dif = ydif 
        zboxes, zdif, same = self._z_split()
        if not same:
            is_same = False
            if zdif > largest_dif:
                best_split = zboxes
                largest_dif = zdif
        return best_split, is_same