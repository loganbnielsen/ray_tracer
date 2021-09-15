from config.Colors import color_rgb_map

class BaseLight:
    def __init__(self, color):
        self.color = color_rgb_map[color]

    def visibility(self):
        # to be initialized by children
        assert False, f"'visibility' method not initialized by {self.__class__}."