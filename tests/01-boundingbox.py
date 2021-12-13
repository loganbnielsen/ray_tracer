import sys
sys.path.append("/home/logan/Documents/cs655/ray_tracer")

from algo.BoundingBox import BoundingBoxSplit
import numpy as np
import inspect

from assets.Sphere import Sphere


def simple_sphere_box():
    assets = [Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1)]
    bb = BoundingBoxSplit(10, 1000)
    boxes = bb.fit(assets)
    for box in boxes:
        print("box", str(box))

def two_sphere_box():
    assets = [Sphere( np.array([ 0.5, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1),
              Sphere( np.array([ 3, -2, 12.5]), 1, "BLUE", "WHITE", 0.1, 0.55, "water", 1)]
    bb = BoundingBoxSplit(1, 1000)
    boxes = bb.fit(assets)
    for box in boxes:
        print("box", str(box))

def main():
    # simple_sphere_box()
    two_sphere_box()


if __name__ == "__main__":
    main()


