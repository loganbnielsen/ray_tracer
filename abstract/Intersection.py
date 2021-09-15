from assets import Asset

class Intersection:
    def __init__(self, obj:Asset, intersect_loc, intersect_ray):
        self.obj = obj
        self.loc = intersect_loc
        self.ray = intersect_ray
