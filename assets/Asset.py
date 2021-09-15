from config.Colors import color_rgb_map

class Asset:
    def __init__(self, diffuse_color, specular_color, reflectivity):
        self.diffuse_color = color_rgb_map[diffuse_color]
        self.specular_color = color_rgb_map[specular_color]
        self.reflectivity = reflectivity

    def intersect(self):
        # This method will be implemented by child class
        assert False, f"'intersect' method not initialized by {self.__class__}."
    
    def normal(self, loc):
        # implemented by child
        assert False, f"'normal' method not initialized by {self.__class__}."