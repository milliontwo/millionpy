class MillionFrame:
    def __init__(self, width, height, data=None):
        self._width = width
        self._height = height
        self._data = data

        if data is None:
            self._data = bytearray(width * height * 2)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def raw_data(self):
        return self._data

    def _check_index(self, x, y):
        """"Throws an exception when the index is out of bounds"""
        if x >= self._width or y >= self._height:
            raise IndexError("Index out of bounds: size (%d : %d) requested: (%d : %d)"
                             % (self._width, self._height, x, y))

    def get_at_index(self, x, y, hand) -> int:
        """"Returns value of the requested hand at the requested position"""

        self._check_index(x, y)

        if hand == 1 or hand == "a":
            return self._data[(y * self._width + x) * 2]
        if hand == 2 or hand == "b":
            return self._data[(y * self._width + x) * 2 + 1]
        return None

    def set_at_index(self, x, y, hand, position):
        """Sets the given value of the hand at the given position"""
        self._check_index(x, y)

        if position > 199 or position < 0:
            raise ValueError('Position should be 0<=Position<200')

        if hand == 1 or hand == 'a':
            self._data[(y * self._width + x) * 2] = position

        if hand == 2 or hand == 'b':
            self._data[(y * self._width + x) * 2 + 1] = position

