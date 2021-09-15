import numpy as np

class Camera:
    x: int
    y: int
    z: int
    position: np.array
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.position = np.array([self.x, self.y, self.z])