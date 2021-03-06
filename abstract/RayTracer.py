from equipment.Camera import Camera
from equipment.Screen import Screen
from theater.Stage import Stage
from theater.Set import Set

from helpers.Methods import camera_rays_generator, jitter_array
from abstract.MaterialRay import MaterialRay
from abstract.Intersection import Intersection
from abstract.PhongIllumination import PhongIllumination
from config.Settings import background_color, is_dry_run, max_parent_rays, is_run_illumination, is_run_reflection, is_run_refraction
from config.Constants import index_of_refraction

import numpy as np

class RayTracer:
    def __init__(self, _set: Set, illumination_model: PhongIllumination):
        self.camera = _set.camera
        self.screen = _set.screen
        self.stage  = _set.stage
        self.illumination_model = illumination_model

    def run(self):
        """
            itterates over camera rays, computing the color at that pixel
        """
        for i, j, n_samples, ray in camera_rays_generator(self.camera, self.screen):
            mray = MaterialRay(self.camera.position, ray, "air", 0)
            mray.ray = jitter_array(mray.ray)
            self.screen.grid.colors[i,j] += self._gen_color(mray) / n_samples

    def _gen_color(self, mray):
        closest_intersect = self.stage.find_closest_intersection(mray.origin, mray.ray)
        if closest_intersect:
            if not is_dry_run:
                color = self._illumination_color(
                    closest_intersect
                )
                reflection_color = self._reflection_color(
                    closest_intersect,
                    mray.medium,
                    mray.count
                )
                refraction_color = self._refraction_color(
                    closest_intersect,
                    mray.medium,
                    mray.count
                )
                # convex combination of object_color and reflection
                if not reflection_color is None:
                    r = closest_intersect.obj.reflectivity
                    color = (1 - r) * color + r * reflection_color
                # convex combination of natural_color and refraction_color
                if not refraction_color is None:
                    r = closest_intersect.obj.refractivity
                    color = (1 - r) * color + r * refraction_color
            else:
                color = closest_intersect.obj.diffuse_color
        else:
            if mray.count == 0:
                color = background_color
            else:
                color = None
        return color

    def _illumination_color(self, intersection:Intersection):
        """
            return rgb_color
        """
        if not is_run_illumination:
            return intersection.obj.diffuse_color
        color = self.illumination_model.run(
            intersection,
            self.stage
        )
        return color

    def _reflection_color(self, intersection:Intersection, medium, count):
        """
            return None OR rgb_color
        """
        # TODO currier to put ray processing on hooks?
        if not is_run_reflection: # check if option is turned on
            return None
        if count + 1 > max_parent_rays: # check if will have too many parents
            return None
        if intersection.obj.reflectivity == 0: # check if trivial
            return None
        mray = MaterialRay(intersection.loc, intersection.reflection(), medium, count+1)
        mray.ray = jitter_array(mray.ray, intersection.obj.glossy_jf)
        return self._gen_color(mray)

    def _gen_refraction_ray(self, n_r, N, V):
        # http://web.cse.ohio-state.edu/~shen.94/681/Site/Slides_files/reflection_refraction.pdf
        inside_sqrt = 1 - n_r**2*(1-np.dot(N,V))
        if inside_sqrt < 0:
            return None
        else:
            return (n_r*np.dot(N,V) - np.sqrt(inside_sqrt))*N - n_r*V

    def _refraction_color(self, intersection: Intersection, previous_medium, count):
        """
            return None OR rgb_color
        """
        if not is_run_refraction: # check if option is turned on
            return None
        if count + 1 > max_parent_rays: # check if will have too many parents
            return None
        if intersection.obj.refractivity == 0: # check if trivial
            return None
        n_r = index_of_refraction[previous_medium] / index_of_refraction[intersection.obj.material]
        refraction_ray  = self._gen_refraction_ray(n_r, intersection.normal(), -intersection.ray)
        if not refraction_ray is None:
            refraction_ray = refraction_ray / np.linalg.norm(refraction_ray)
            mray = MaterialRay(intersection.loc, refraction_ray, intersection.obj.material, count+1)
            mray.ray = jitter_array(mray.ray, intersection.obj.translucency_jf)
            return self._gen_color(mray)
        else:
            return None
        