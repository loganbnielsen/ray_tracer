from config.Colors import color_rgb_map

class Asset:
    def __init__(self, diffuse_color, specular_color, reflectivity, refractivity, material, jitter_factor):
        self.diffuse_color = color_rgb_map[diffuse_color]
        self.specular_color = color_rgb_map[specular_color]
        self.reflectivity = reflectivity
        self.refractivity = refractivity
        self.material = material
        self.jitter_factor = jitter_factor

    def intersect(self):
        # This method will be implemented by child class
        assert False, f"'intersect' method not initialized by {self.__class__}."
    
    def normal(self, loc):
        # implemented by child
        assert False, f"'normal' method not initialized by {self.__class__}."
    
    @property
    def x_min(self):
        # defined by child
        assert False, f"'x_min' method not initialized by {self.__class__}."
    
    @property
    def x_max(self):
        # implemented by child
        assert False, f"'x_max' method not initialized by {self.__class__}."

    @property
    def y_min(self):
        # implemented by child
        assert False, f"'y_min' method not initialized by {self.__class__}."

    @property
    def y_max(self):
        # implemented by child
        assert False, f"'y_max' method not initialized by {self.__class__}."

    @property
    def z_min(self):
        # implemented by child
        assert False, f"'z_min' method not initialized by {self.__class__}."

    @property
    def z_max(self):
        # implemented by child
        assert False, f"'z_max' method not initialized by {self.__class__}."
