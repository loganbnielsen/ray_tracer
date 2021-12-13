from copy import deepcopy

class EarClipper:
    def __init__(self):
        pass

    def clip(self, vertices):
        """
            vertices is a list of vertices where edges are between
            each element with the last vertex connecting to the first
            one

            returns a list of list of coordinates defining triangles [[coord1, coord2, np coord3], ...]
        """
        assert len(vertices) > 2, "Must have at least 3 vertices to convert to triangles."
        vertices = deepcopy(vertices) # make a copy of the vertices so the originals aren't modified

        triangles = []
        while len(vertices) > 3:
            tri, i = self._find_triangle(vertices)
            triangles.append(tri)
            del vertices[i]
        triangles.append(vertices)
        return triangles
    
    def _find_triangle(self, vertices):
        triangle,i = self._find_triangle_helper(vertices)
        if triangle is None:
            vertices = self._swap_yz(vertices)
            triangle,i = self._find_triangle_helper(vertices)
            vertices = self._swap_yz(vertices) # triangle is made of pointers from vertices so vertices should be flipped automatically
            if triangle is None:
                vertices = self._swap_xz(vertices)
                triangle,i = self._find_triangle_helper(vertices)
                vertices = self._swap_xz(vertices) # triangle is made of pointers from vertices so vertices should be flipped automatically
                if triangle is None:
                    raise(f"Unable to find a triangle and expected to find one. Vertices are: {vertices}.")
        return triangle,i

    def _find_triangle_helper(self, vertices):
        triangle = None
        for i in range(len(vertices)-1):
            midpoint = (vertices[i-1] + vertices[i+1])/2
            _v_subset = [vertices[i-1], vertices[i], vertices[i+1]]
            isvalid = self._forms_valid_triangle(_v_subset, midpoint)
            if isvalid:
                triangle = [vertices[i-1],vertices[i], vertices[i+1]]
                break
        return triangle,i

    def _swap_yz(self, l):
        for i in range(len(l)):
            l[i][1],l[i][2] = l[i][2],l[i][1]
        return l

    def _swap_xz(self, l):
        for i in range(len(l)):
            l[i][0],l[i][2] = l[i][2],l[i][0]
        return l
    
    def _forms_valid_triangle(self, vertices, midpoint):
        n_crosses = 0
        centered_vertices = [v - midpoint for v in vertices]
        for i in range(len(centered_vertices)):
            x1, y1 = centered_vertices[i-1][0], centered_vertices[i-1][1]
            x2, y2 = centered_vertices[i][0], centered_vertices[i][1]
            # we want to know if it crosses the y-axis an odd or even number of times
            # on the positive side of the x-axis
            if x2 > 0 or x1 > 0: # at least part of the line is in the positive x plane
                if y1 * y2 < 0: # crossed the y axis
                    if x1 >= 0 and x2 >= 0: # passed the y axis on the positive side of the x-axis
                        n_crosses += 1
                    else: # it may or may not have crossed on the positive side of the x-axis
                        m = (y2 - y1)/(x2 - x1) if x2 - x1 != 0 else (y2 - y1)/1e-8
                        b = y1 - m*x1
                        if m < 0 and b >= 0: # line is downward-sloping, at x=0 it's above the y-axis
                            n_crosses += 1
                        elif m > 0 and b <= 0: # line is upward-sloping, at x=0 it's below the y-axis
                            n_crosses += 1
        return n_crosses % 2 == 1
