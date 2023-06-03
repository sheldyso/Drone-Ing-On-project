import numpy as np

class Vector_3D():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

class Vector_2D():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class matrix_4x4():
    def __init__(self) -> None:
        self.identity = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ])

class matrix_3x3():
    def __init__(self) -> None:
            self.identity = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            ])

