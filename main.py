from equipment.Camera import Camera
from equipment.Screen import Screen

from theater.Stage import Stage
from theater.Set import Set

from helpers.Methods import camera_rays_generator, save_img
from config.Init import objects as objs, directional_lights
from config.Settings import CameraPosition as cp, ScreenSize as ss

from config.Constants import phong_illumination_constants

from abstract.RayTracer import RayTracer
from abstract.PhongIllumination import PhongIllumination 

def setup():
    # equipment
    camera = Camera(cp.x, cp.y, cp.z)
    screen = Screen(ss.height, ss.width, ss.samples_per_pixel)
    # stage
    stage = Stage(objs, directional_lights)
    return Set(camera, screen, stage), PhongIllumination(**phong_illumination_constants)

def main():
    _set, illumination_model = setup()
    ray_tracer = RayTracer(_set, illumination_model)
    ray_tracer.run()
    save_img(ray_tracer.screen.grid.colors)
    

if __name__ == "__main__":
    main()