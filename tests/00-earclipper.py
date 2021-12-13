import sys
sys.path.append("/home/logan/Documents/cs655/ray_tracer")

from algo.EarClipper import EarClipper
import numpy as np
import inspect


def z_0_square_test():
    print(inspect.stack()[0][3])
    vertices = [np.array([0,0,0]),np.array([0,1,0]),np.array([1,1,0]),np.array([1,0,0])]
    triangles = EarClipper().clip(vertices)
    print(triangles)

def house_test():
    print(inspect.stack()[0][3])
    vertices = [np.array([0,0,0]),np.array([0,1,0]),np.array([.5,2,0]),np.array([1,1,0]),np.array([1,0,0])]
    triangles = EarClipper().clip(vertices)
    print(triangles)

def y_0_square_test():
    print(inspect.stack()[0][3])
    vertices = [np.array([0,0,0]),np.array([0,0,1]),np.array([1,0,1]),np.array([1,0,0])]
    triangles = EarClipper().clip(vertices)
    print(triangles)

def x_0_square_test():
    print(inspect.stack()[0][3])
    vertices = [np.array([0,0,0]),np.array([0,1,0]),np.array([0,1,1]),np.array([0,0,1])]
    triangles = EarClipper().clip(vertices)
    print(triangles)


def main():
    z_0_square_test()
    y_0_square_test()
    x_0_square_test()
    house_test()

if __name__ == "__main__":
    main()