
class MaterialRay:
    def __init__(self, origin, ray, medium, count):
        """
            medium: The material being traveled through
            count: number of parent rays (i.e. parents could be camera (root node), reflection, refraction)
        """
        self.origin = origin
        self.ray = ray
        self.medium = medium
        self.count = count