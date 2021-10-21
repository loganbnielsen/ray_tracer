import numpy as np
from assets.Asset import Asset
from helpers.Methods import offset_vector, euclid_length
from config.Constants import EPSILON

class Triangle(Asset):
    def __init__(self, vtx0, vtx1, vtx2, diffuse_color, specular_color, reflectivity, refractivity, material, jitter_factor):
        super().__init__(diffuse_color, specular_color, reflectivity, refractivity, material, jitter_factor)
        self.vtx0 = vtx0
        self.vtx1 = vtx1
        self.vtx2 = vtx2

        self.edge1 = self.vtx1 - self.vtx0
        self.edge2 = self.vtx2 - self.vtx0

    def intersect(self, origin, ray):
        # https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm
        offset_origin = offset_vector(origin, ray)
        h = np.cross(ray, self.edge2)
        a = np.dot(self.edge1, h)
        if a > -EPSILON and a < EPSILON:
            return # ray is parallel to the triangle
        f = 1/a
        s = offset_origin - self.vtx0
        u = f * np.dot(s,h)
        if u < 0 or u > 1:
            return
        q = np.cross(s, self.edge1)
        v = f * np.dot(ray, q)
        if v < 0 or u + v > 1:
            return
        # compute t to find intersection point
        t = f * np.dot( self.edge2, q)
        if t > EPSILON:
            # print(f"Triangle t: {t}")
            # ray intersection
            return t
        else:
            # line intersection but not ray intersection
            return

    def normal(self, loc):
        n = np.cross(self.edge1, self.edge2)
        n = n / euclid_length(n)
        return n