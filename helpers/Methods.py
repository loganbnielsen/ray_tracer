import numpy as np
from pathlib import Path

from equipment.Camera import Camera
from equipment.Screen import Screen

from PIL import Image
from imageio import imwrite
from tqdm import tqdm

from config.Settings import jitter_factor

def camera_rays_generator(camera: Camera, screen : Screen):
    n_samples = np.sqrt( screen.samples_per_pixel ).astype(int)
    assert np.isclose(n_samples, np.sqrt( screen.samples_per_pixel ))
    nx, ny, _ = screen.grid.coords.shape
    tqdm()
    for i in tqdm(range(nx*n_samples), desc="Row", leave=False):
        i = i//n_samples
        for j in range(ny*n_samples):
            j = j//n_samples
            ray = screen.grid.coords[i,j,:] - camera.position
            u_ray = ray / euclid_length(ray)
            yield i, j, n_samples, u_ray

def offset_vector(origin, ray):
    return origin + ray * 1e-5

def reflection_ray(input_array, normal):
    """
        input_array should be pointing AWAY from the point of intersection
        normal is the normal of the surface the input_array is reflecting off of
    """
    return 2 * normal * np.dot(normal, input_array) - input_array

def save_img(arr):
    arr = np.transpose(arr, (1,0,2))
    arr = arr * 255/np.max(arr)
    arr = arr.astype('uint8')
    im = Image.fromarray(arr)
    Path("out/img/").mkdir(parents=True, exist_ok=True)
    im.save("out/img/foo1.jpg")
    imwrite('out/img/foo1.ppm', arr, format='PPMRAW-FI', flags=1)

def jitter_array(arr, scale=1):
    """
        jitter's array if jitter_factor is non-zero
    """
    total_jitter_factor = jitter_factor*scale
    if total_jitter_factor != 0:
        assert total_jitter_factor == jitter_factor, f"total jitter factor is {total_jitter_factor}"
        noise = np.random.normal(0, total_jitter_factor, arr.shape)
        jit = arr + noise 
        return jit / euclid_length(jit)
    else:
        return arr

def euclid_length(v):
    return sum(v*v)**0.5
