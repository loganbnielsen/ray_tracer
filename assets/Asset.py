from config.Colors import color_rgb_map

class Asset:
    def __init__(self, diffuse_color, specular_color, reflectivity, refractivity, material,
                 glossy_jf, translucency_jf): # jf = jitter factor
        self.diffuse_color = color_rgb_map.get(diffuse_color)
        self.specular_color = color_rgb_map.get(specular_color)
        self.reflectivity = reflectivity
        self.refractivity = refractivity
        self.material = material
        self.glossy_jf = glossy_jf
        self.translucency_jf = translucency_jf
        # these attributes should be set by child (TODO implement as property methods)
        self.min_x = None
        self.min_y = None
        self.min_z = None
        self.max_x = None
        self.max_y = None
        self.max_z = None
        

    def intersect(self):
        # This method will be implemented by child class
        assert False, f"'intersect' method not initialized by {self.__class__}."
    
    def normal(self, loc):
        # implemented by child
        assert False, f"'normal' method not initialized by {self.__class__}."
    
    # TODO figure out best way to handle this
    # @property
    # def min_x(self):
    #     # defined by child
    #     assert False, f"'x_min' method not initialized by {self.__class__}."
    
    # @property
    # def max_x(self):
    #     # implemented by child
    #     assert False, f"'x_max' method not initialized by {self.__class__}."

    # @property
    # def min_y(self):
    #     # implemented by child
    #     assert False, f"'y_min' method not initialized by {self.__class__}."

    # @property
    # def max_y(self):
    #     # implemented by child
    #     assert False, f"'y_max' method not initialized by {self.__class__}."

    # @property
    # def min_z(self):
    #     # implemented by child
    #     assert False, f"'z_min' method not initialized by {self.__class__}."

    # @property
    # def max_z(self):
    #     # implemented by child
    #     assert False, f"'z_max' method not initialized by {self.__class__}."
