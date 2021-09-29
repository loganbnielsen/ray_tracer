import numpy as np

from equipment.Camera import Camera

class Screen:
    samples_per_pixel: int
    height : int
    width : int
    aspect_ratio : float
    left : np.array
    top : np.array
    right : np.array
    bottom : np.array
    bottom_left : np.array
    top_left : np.array
    top_right : np.array
    bottom_right  : np.array
    min_x : int
    max_x : int
    min_y : float
    max_y : float
    pixelgrid : np.array

    
    def __init__(self, height, width, samples_per_pixel):
        self.samples_per_pixel = samples_per_pixel
        self.height = height
        self.width  = width
        self.aspect_ratio = self.width / self.height
        # middle of edge lenghts
        self.left   = np.array([-1,0,0]) # x y z
        self.top    = np.array([0,self.aspect_ratio**-1,0])
        self.right  = -self.left
        self.bottom = -self.top
        # corners
        self.bottom_left  = np.array([-1,-self.aspect_ratio**-1, 0])
        self.top_left     = np.array([-1, self.aspect_ratio**-1, 0])
        self.top_right    = np.array([ 1, self.aspect_ratio**-1, 0])
        self.bottom_right = np.array([ 1,-self.aspect_ratio**-1, 0])
        # useful
        self.min_x = -1
        self.max_x =  1
        self.min_y = -self.aspect_ratio**-1
        self.max_y =  self.aspect_ratio**-1
        # generate pixelgrid
        self.grid = Grid(self.min_x, self.max_x, self.min_y, self.max_y, self.height, self.width, self.samples_per_pixel)


class Grid:
    def __init__(self, min_x, max_x, min_y, max_y, height, width, samples_per_pixel):
        self.coords = self._gen_coords(min_x, max_x, min_y, max_y, height, width, samples_per_pixel)
        self.colors = np.zeros(self.coords.shape) # RGB channels
    
    def _gen_coords(self, min_x, max_x, min_y, max_y, height, width, samples_per_pixel):
        """
            coords -- contains the point in space that represents the center of the top left pixel at index [0,0]
            the coordinates of the center of the top-right pixel are stored at pixelgrid[width, 0]
            the center of the bottom-left pixel are stored at pixelgrid[0, height]
            the center of the bottom-right pixel are stored at pixelgrid[width, height]
            coordinates are in (x,y,z) format
        """
        def _axis_array(min_val, max_val, n):
            """
                Creates an axis where the values of the indices are locations in space.
                When initilialized, these values start off as the bottom/left of the points in space (e.g. [0,1,2,3,4])
                They're shifted so that the index now corresponds to the center point in space (e.g. [0.5,1.5,2.5,3.5,4.5])
            """
            virtual_n = n * np.sqrt( samples_per_pixel ).astype(int)
            line = np.linspace(min_val, max_val, virtual_n, endpoint=False) # (bottom/left) side of each pixel starting from (bottom/left)
            width = line[1] - line[0]
            centered = line + width/2
            return centered

        y_line = _axis_array(min_y, max_y, height)[::-1] # first index is now top. (without ::-1 would start from the bottom)
        x_line = _axis_array(min_x, max_x, width)

        coords = np.stack([np.zeros((len(x_line), len(y_line)))]*3, axis=2)
        for i, x in enumerate(x_line): # x starts from left
            for j, y in enumerate(y_line):
                coords[i,j,:] = np.array([x,y,0])
        return coords

