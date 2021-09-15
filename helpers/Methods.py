import numpy as np

from equipment.Camera import Camera
from equipment.Screen import Screen

from PIL import Image

from imageio import imwrite

def camera_rays_generator(camera: Camera, screen : Screen):
    nx, ny, _ = screen.grid.coords.shape
    for i in range(nx):
        for j in range(ny):
            ray = screen.grid.coords[i,j,:] - camera.position
            u_ray = ray / np.linalg.norm(ray)
            yield i, j, u_ray

def offset_vector(origin, ray):
    return origin + ray * 1e-5

def save_img(arr):
    arr = np.transpose(arr, (1,0,2))
    arr = arr * 255/np.max(arr)
    print(arr)
    arr = arr.astype('uint8')
    print("-----------")
    print(arr)
    im = Image.fromarray(arr)
    im.save("out/img/foo1.jpg")
    imwrite('out/img/foo1.ppm', arr, format='PPMRAW-FI', flags=1)
