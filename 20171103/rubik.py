# 90 degree rotations in the XY plane. CW is clockwise, CC is counter-clockwise.
ROT_XY_CW = Matrix(0, 1, 0,
                   -1, 0, 0,
                   0, 0, 1)
ROT_XY_CC = Matrix(0, -1, 0,
                   1, 0, 0,
                   0, 0, 1)

# 90 degree rotations in the XZ plane (around the y-axis when viewed pointing toward you).
ROT_XZ_CW = Matrix(0, 0, -1,
                   0, 1, 0,
                   1, 0, 0)
ROT_XZ_CC = Matrix(0, 0, 1,
                   0, 1, 0,
                   -1, 0, 0)

# 90 degree rotations in the YZ plane (around the x-axis when viewed pointing toward you).
ROT_YZ_CW = Matrix(1, 0, 0,
                   0, 0, 1,
                   0, -1, 0)
ROT_YZ_CC = Matrix(1, 0, 0,
                   0, 0, -1,
                   0, 1, 0)

def get_rot_from_face(face):
    """
    :param face: One of FRONT, BACK, LEFT, RIGHT, UP, DOWN
    :return: A pair (CW, CC) given the clockwise and counterclockwise rotations for that face
    """
    if face == RIGHT:   return "R", "Ri"
    elif face == LEFT:  return "L", "Li"
    elif face == UP:    return "U", "Ui"
    elif face == DOWN:  return "D", "Di"
    elif face == FRONT: return "F", "Fi"
    elif face == BACK:  return "B", "Bi"
    return None


def is_solved(self):
        def check(colors):
            assert len(colors) == 4
            return all(c == colors[0] for c in colors)
        return (check([piece.colors[2] for piece in self._face(FRONT)]) and
                check([piece.colors[2] for piece in self._face(BACK)]) and
                check([piece.colors[1] for piece in self._face(UP)]) and
                check([piece.colors[1] for piece in self._face(DOWN)]) and
                check([piece.colors[0] for piece in self._face(LEFT)]) and
                check([piece.colors[0] for piece in self._face(RIGHT)]))
